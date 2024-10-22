# certaintimes

Tool for logging UTC times of user actions/observations.

This is motivated by two main use cases:

- Keeping track of how long a test session takes
- Recording timestamps to aid debugging problems using product logs

For the first, times are echoed and logging using HH:MM:SS since the start of the session.

For the second, UTC timestamped events are appended to certaintimes.log.

## Example session

User interaction:

```
$ certaintimes
Enter text to append it as a UTC timed log entry to certaintimes.log, q or quit to exit.

local time: 2023-07-19 12:32:23.695581
       UTC: 2023-07-19 11:32:23.695586+00:00

IMPORTANT: WSL can get out of sync over sleep!
If this time does not look close, please exit and fix e.g. with 'sudo hwclock -s'
ST session to test upgrade
00:00:05 ST session to test upgrade
Start upgrade
00:00:12 Start upgrade
Upgrade failed to start!
00:00:17 Upgrade failed to start!
q
```

Corresponding log entries in certaintimes.log:

``` log
2023-07-19T11:32:23.695Z 00:00:00 ====== Starting session ======
2023-07-19T11:32:29.066Z 00:00:05 ST session to test upgrade
2023-07-19T11:32:36.083Z 00:00:12 Start upgrade
2023-07-19T11:32:41.489Z 00:00:17 Upgrade failed to start!
2023-07-19T11:32:42.552Z 00:00:18 ====== Ending session ======
```

## Multiple observers

If you are running a test session with multiple observers you can record to files with
the observer name in the filename and prefixed to each log line.

```
$ certaintimes -o alice
Enter text to append it as a UTC timed log entry to certaintimes-alice.log, q or quit to exit.

local time: 2023-07-19 12:33:37.169516
       UTC: 2023-07-19 11:33:37.169522+00:00

IMPORTANT: WSL can get out of sync over sleep!
If this time does not look close, please exit and fix e.g. with 'sudo hwclock -s'
ST session to test certaintimes with named observers
00:00:14 ST session to test certaintimes with named observers
Time entries as before
00:00:19 Time entries as before
Should record to file with observer name
00:00:32 Should record to file with observer name
q
```

Corresponding log entries in certaintimes-alice.log:

``` log
2023-07-19T11:33:37.170Z alice: 00:00:00 ====== Starting session ======
2023-07-19T11:33:51.193Z alice: 00:00:14 ST session to test certaintimes with named observers
2023-07-19T11:33:57.098Z alice: 00:00:19 Time entries as before
2023-07-19T11:34:09.928Z alice: 00:00:32 Should record to file with observer name
2023-07-19T11:34:11.155Z alice: 00:00:33 ====== Ending session ======
```

# Development

Use poetry to create a virtual environment to develop in:

``` bash
poetry install
poetry update
```

## Running development versions

Use poetry run to run development versions e.g.

``` bash
poetry run certaintimes
```

## Running unit tests

``` bash
poetry run pytest
```

## Auto format code

``` bash
poetry run black certaintimes
```


## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft
trademarks or logos is subject to and must follow
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
