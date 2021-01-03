# Creating a Service

Create a service configuration file under `/etc/systemd/system/` with extension `.service`.

```
[Unit]
Description=<description>
After=<After which service to start; optional>
StartLimitIntervalSec=0 (keep restarting service as long as it does not turn on)
Type=simple
Restart=<always|on-failure, optional> 
RestartSec=<no. of seconds to wait before restart, optional>
User=<User name>
ExecStart=<What to execute>

[Install]
WantedBy=multi-user.target
```
