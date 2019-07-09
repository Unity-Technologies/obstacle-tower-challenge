# FAQ / Troubleshooting

## Getting `UnityTimeOutException` upon submission ([discussion here](https://discourse.aicrowd.com/t/unitytimeoutexception-in-evaluation/1035))

* Try increasing `timeout_wait` when creating `ObstacleTowerEnv` from original `30` to `300` or even higher.
* Start your agent code by first creating the `ObstacleTowerEnv` object before anything else (including larger imports).
    If you create the environment "too late", it may have issues connecting to the OT binary running for evaluation.

## Getting "No module named ..." for common packages (e.g. Numpy) ([discussion here](https://discourse.aicrowd.com/t/solved-no-module-named-numpy-or-similar/1238)]

* If you are using older version of the `run.sh` example, remove/comment out part with `source activate base`. 

## Issues with aicrowd-repo2docker

* Try updating aicrowd-repo2docker (`pip install -U aicrowd-repo2docker`)
* aicrowd-repo2docker ships with Python 3.7 by default. `mlagents-env` does not (as of writing) work with Py37.
  You can fix this by adding `python-3.6` to `runtime.txt` in root of your submission code directory.
  [More details here](https://discourse.aicrowd.com/t/announcement-aicrowd-repo2docker-base-image-update/1195).

## Zero score in leaderboard

* Make sure you have debug mode disabled in `aicrowd.json`. Debug mode forces leaderboard score to zero.

