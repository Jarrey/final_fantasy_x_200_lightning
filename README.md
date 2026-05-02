# Final Fantasy X 200 Times Lightning Automation

This project is a Raspberry Pi-based hardware automation inspired by the article:
"Using Raspberry Pi, a photosensor, and a small servo to automatically earn the Final Fantasy X HD Remaster 200 lightning avoidance trophy."

The script in `run.py` reads a light sensor and drives a small servo to press the O button on a PSV screen as soon as the lightning flash is detected.

For a Chinese version of the README, see [README_zh.md](README_zh.md).

## Overview

Final Fantasy X HD Remaster requires extremely fast and consistent timing to complete the 200 lightning avoidance challenge. This project uses a Raspberry Pi, a light-dependent resistor (LDR) sensor, and a small servo to automatically detect the flash and press the button.

## Hardware

- Raspberry Pi with GPIO support
- Light-dependent resistor (LDR) or photosensor module with built-in analog output
- Small hobby servo motor
- Wiring or breadboard connections
- Power supply for Raspberry Pi and servo

## Wiring

The hardware wiring follows the article's implementation:

- `GPIO 4` is used for the light sensor input
- `GPIO 18` is used for the servo PWM control

The light sensor is connected through a GPIO pin so the Pi can detect low-level changes when the flash occurs.
The servo signal pin is connected to the PWM-capable `GPIO 18` pin.

### Visual diagrams

Achievement screenshot:

![Achievement](img/achievement.jpg)

Circuit connection photo:

![Circuit](img/circuit.jpg)

Raspberry Pi GPIO pinout diagram:

![GPIO Pinout](img/gpio-pinout.png)

## Software

The main file is `run.py`. It contains the following behavior:

- configure GPIO mode to `GPIO.BCM`
- initialize the servo on `servoPin = 18`
- prepare the light sensor on `lightPin = 4`
- read the sensor value continuously
- when the light sensor reads `GPIO.LOW`, perform a quick servo motion sequence

The servo sequence in the script is:

- move to angle 30
- wait 0.1 seconds
- move to angle 60
- wait 0.1 seconds
- move back to angle 30
- wait 0.1 seconds

This sequence is intended to physically press the O button and release it quickly.

## How it works

1. The photosensor watches the PSV screen for the lightning flash.
2. When the flash makes the light sensor output change, Raspberry Pi detects a low signal on `GPIO 4`.
3. The servo motor is driven by PWM on `GPIO 18`.
4. The servo moves in a short pulse to tap the button and returns to its original position.
5. The script counts repetitions and continues until manually stopped.

## Notes

- The exact servo angles may need fine-tuning for your particular servo and button mechanism.
- If your light sensor module does not include a built-in ADC, you must add an ADC conversion stage or use a compatible sensor.
- Make sure the servo power supply is stable. If the servo draws too much current, use a separate supply or add resistors as needed.

## Run instructions

Run the project on a Raspberry Pi with the required GPIO library installed:

```bash
python run.py
```

Press `Ctrl+C` to stop the script.

## Reference

CNBlogs:
https://www.cnblogs.com/wpf_gd/articles/4700789.html

The article shows the complete idea, hardware setup, and example code for automating the Final Fantasy X 200 lightning avoidance trophy using Raspberry Pi.
