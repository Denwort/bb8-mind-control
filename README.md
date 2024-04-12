# BB8 Project

The objective of this project is to control a small BB8 robot using mental commands.

## Files
- [`cortex.py`](./cortex.py) - The wrapper library around the EMOTIV Cortex API. More details [here](https://github.com/Emotiv/cortex-example).
- [`train.py`](./train.py) - Trains a profile to recognize the specified mental commands. More details [here](https://emotiv.gitbook.io/cortex-api/bci).
- [`live.py`](./live.py) - Shows the mental command action in live mode. More details [here](https://emotiv.gitbook.io/cortex-api/advanced-bci).
- [`sphero.py`](./sphero.py) - Controls the Sphero BB8. Moves the robot according to the mental command received. More details: [here](https://spherov2.readthedocs.io/en/latest/sphero_edu.html).

## Requirements
- Epoc X Headset
- Sphero BB8
- Python >= 3.7
- Install the Python requirements via `pip install -r requirements.txt`

## How to Run

To run the live mode of the Epoc X headset, you will need to do a few things:

1. Next, [download and install](https://www.emotiv.com/developer/) the Cortex service. Please note that currently, the Cortex service is only available for Windows and macOS.
2. Login via the EMOTIV Launcher. If you don't have an EmotivID, you can [register here](https://id.emotivcloud.com/eoidc/account/registration/). Then you can plug in the dongle, press the Epoc X button, and pair the device.
3. Next, to get a client ID and a client secret, you must connect to your Emotiv account on [emotiv.com](https://account.emotiv.com/my-account/cortex-apps/) and create a new Cortex app.
4. Finally, the first time you run these examples, you also need to authorize them in the EMOTIV Launcher. You must paste the client ID and client secret in the code of the example that you want to run. You may also need a profile name if required.
5. To train a profile, we suggest using the EmotivBCI app. It allows visualization of the command differences and makes training easier. However, you can also use `train.py` which will train the profile using the commands given on the actions array.
6. After training, you can now run `live_advanced.py` which will collect the mental command data and send it via UDP.

**Note:** If you encounter a strange bug that disconnects the headset when you attempt to run live.py, try closing all EMOTIV apps except the EMOTIV Launcher. Then, manually disconnect and reconnect the headset. Afterward, try running live.py again, and it should work properly.

To run the Sphero BB8, you will need to do a few more steps:

1. Take the robot out of its charging station to turn it on.
2. Next, turn on the Bluetooth and pair the BB8. The light should become blue.
3. You can now run `sphero.py` which will receive the mental command data and move the BB8 according to the user's thoughts. Note that `live.py` and `sphero.py` must run simultaneously.