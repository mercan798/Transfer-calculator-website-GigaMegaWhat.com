# Transfer-calculator-website-GigaMegaWhat.com




# TB Data Transfer Time Calculator

A Gradio-based web application that calculates how long it takes to transfer data based on file size (in Terabytes) and connection speed (in Mbit/s).

## Features

- Calculate transfer time for large data amounts
- Input data size in TB and connection speed in Mbit/s
- Results displayed in days, hours, minutes, and seconds
- Simple and intuitive web interface
- Input validation and error handling

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/tb-transfer-calculator.git
cd tb-transfer-calculator
```

2. Install dependencies:
```bash
pip install gradio
```

3. Set up configuration:
```bash
cp config.example.py config.py
```

4. Edit `config.py` with your AdSense credentials:
```python
ADSENSE_CLIENT = "ca-pub-XXXXXXXXXXXXXXXX"
ADSENSE_SLOT = "XXXXXXXXXX"
```

## Usage

Run the application:
```bash
python trans.py
```

The app will open in your browser. Enter the data size in TB, connection speed in Mbit/s, and click "Hesap" to calculate.

## Configuration

- `config.py` - Contains your AdSense credentials (not tracked by git)
- `config.example.py` - Template file for configuration

**Important:** Never commit `config.py` to GitHub. It's already in `.gitignore`.

## License
