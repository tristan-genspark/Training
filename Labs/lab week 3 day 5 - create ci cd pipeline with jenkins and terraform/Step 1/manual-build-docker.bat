@echo OFF
cd "Build-Server"
docker build --no-cache -t http-py-server .
echo.
echo To run the container continue this script
pause
docker run -d -p 8081:80 http-py-server
pause
