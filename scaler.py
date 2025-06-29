import pandas as pd
import re

INPUT_CSV = 'Netze-Strom-Lastprofil-SH0_2024.csv'


def scale_df_annual(df: pd.DataFrame, required_annual_consumption: float):
    """
    Scale a 15-minute‐interval Load profile so that its total energy matches the required annual consumption.
    Returns scaled DataFrame and the scaling factor.
    """
    current_annual = df['Load'].sum() * 0.25
    scaler = required_annual_consumption / current_annual
    df_scaled = df.copy()
    df_scaled['scaled_load'] = df_scaled['Load'] * scaler
    return df_scaled, scaler


def sanitize_filename(value):
    # Remove non-alphanumeric characters except dot and underscore
    return re.sub(r'[^\w\.-]', '_', str(value))


def process_and_save(df, target):
    try:
        target_float = float(target)
    except ValueError:
        print(f'Invalid input: {target}. Skipping.')
        return
    df_scaled, scale_factor = scale_df_annual(df, target_float)
    print(f'Applied scaler: {scale_factor:.4f} for target {target}')
    print('New annual total:', df_scaled['scaled_load'].sum() * 0.25, 'kWh')
    safe_target = sanitize_filename(target)
    output_csv = f'Netze-Strom-Lastprofil-SH0_2024_scaled_{safe_target}.csv'
    df_scaled[["scaled_load"]].to_csv(output_csv, index=True)
    print(f'Scaled profile saved to {output_csv}\n')


def main():
    # Read CSV as strings, then combine date and time columns
    df = pd.read_csv(
        INPUT_CSV,
        sep=';',
        decimal=',',
        dayfirst=True,
        dtype={'Ab-Datum': str, 'Ab-Zeit': str}
    )
    # Combine date and time columns into a single datetime
    df['Datetime'] = pd.to_datetime(df['Ab-Datum'] + ' ' + df['Ab-Zeit'], dayfirst=True)
    df = df.set_index('Datetime')
    df.rename(columns={'Profilwert': 'Load'}, inplace=True)
    df['Load'] = df['Load'].astype(float)
    df = df[['Load']]
    df = df * 1000  # match notebook logic

    while True:
        target = input('Enter desired annual consumption in kWh (single value or comma-separated list, blank to exit): ')
        if not target.strip():
            print('Exiting.')
            break
        targets = [t.strip() for t in target.split(',') if t.strip()]
        for t in targets:
            process_and_save(df, t)


if __name__ == '__main__':
    main() 