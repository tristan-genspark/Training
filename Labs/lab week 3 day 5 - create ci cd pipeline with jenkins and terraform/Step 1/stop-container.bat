@echo OFF

docker ps -a -q > containers.tmp

set /p containers= < containers.tmp

del containers.tmp

docker stop %containers%

docker rm %containers%
