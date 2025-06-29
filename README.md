# SHO_SCALER: Annual Load Profile Scaler

This tool allows you to scale a 15-minute interval load profile (from a CSV file) to match a desired annual energy consumption. It is designed for easy use and sharing with team members, including those with minimal technical experience.

## Features
- Reads a load profile from `Netze-Strom-Lastprofil-SH0_2024.csv`.
- Prompts for a target annual consumption (in kWh).
- **You can enter a single value (e.g., `10000`) or a list of values separated by commas (e.g., `10000, 5000, 7500`).**
- Scales the profile accordingly for each value entered.
- **Creates a new scaled profile CSV for each target value, with the target in the filename (e.g., `Netze-Strom-Lastprofil-SH0_2024_scaled_10000.csv`).**
- Allows repeated scaling with different targets in one session.

## Requirements
- Python 3.9 or higher
- pandas (see `requirements.txt`)

## Installation
1. Download or copy all the files in this folder to your computer.
2. Open a terminal (Command Prompt on Windows, Terminal on Mac/Linux) and navigate to the folder containing these files.
3. Install the required Python package by running:

   ```bash
   pip install -r requirements.txt
   ```

   If you get an error about `pip` not being found, try `python -m pip install -r requirements.txt` instead.

## Usage
1. Make sure your input file `Netze-Strom-Lastprofil-SH0_2024.csv` is in the same folder as `scaler.py`.
2. Run the script:

   **On Windows:**
   ```bash
   python scaler.py
   ```
   **On Mac/Linux:**
   ```bash
   python3 scaler.py
   ```
3. When prompted, enter your desired annual consumption(s) in kWh:
   - For a single value, type something like `10000` and press Enter.
   - For multiple values, type them separated by commas, like `10000, 5000, 7500` and press Enter.
4. The script will create a new CSV file for each value you entered, with the value included in the filename (e.g., `Netze-Strom-Lastprofil-SH0_2024_scaled_10000.csv`).
5. You can repeat the process with new values, or just press Enter on a blank line to exit.

## Output
- For each value you enter, you will get a file named like `Netze-Strom-Lastprofil-SH0_2024_scaled_<target>.csv`, containing the datetime index and the new `scaled_load` column for the specified annual consumption.

## Troubleshooting
- If you see an error about missing `pandas`, make sure you have run the installation step above.
- If you have trouble running the script, check that you are in the correct folder and that your input CSV is present.
- If you enter something that is not a number, the script will skip it and continue.

## License
This project is provided for internal use. Please contact the author for external distribution. 
