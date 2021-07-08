<h1>Server, Self-Hosting, and Adding Functions</h1>
<p>
  The entire backend of this project is a Python Flask server, hosted on a <a href="http://hershyz.pythonanywhere.com">PythonAnywhere</a> server.
  
  <strong>Server Requirements</strong>
  <pre>
    <a href="https://www.python.org/downloads/">Python >=  3.7.6</a>
    Flask      (pip install flask)
    Yfinance   (pip install yfinance)
    
    All packages can be installed with pip (included with Python by default).
    Flask and Yfinance have their own dependencies, but should be installed along with their respective pip commands.
  </pre>
  
  <strong>Directory Structure</strong>
  <pre>
    /server (root)
      |- options      (data storage for options)
      |- stocks       (data storage for stocks)
      |- ...
      |- app.py       (API entry point, Flask endpoint handler)
      |- ...
      |- symbols.txt  (storage for target stock symbols)
      |- ...
      |- (other source files)
  </pre>
  
  <strong>Self-Hosting</strong>
  <pre>
    cd server
    python app.py
    ...
    Flask will provide a localhost HTTP address, which can then be tested from cURL or the <a href="https://github.com/hershyz/hamoc-tools/blob/main/docs/api-wrapper.md">api wrapper</a>.
  </pre>
  
   <strong>Adding Functions</strong>
    <pre>
      All functions are stored as endpoints, which are routed by Flask.
      The HTTP methods to an endpoint can be specified, GET for fetching data, POST for doing anything else server-side.
      ...
      Adding an endpoint to the <a href="https://github.com/hershyz/hamoc-tools/blob/main/server/app.py">main file</a> can be done like <a href="https://github.com/hershyz/hamoc-tools/blob/main/docs/endpoints.py">so</a>.
    </pre>
</p>
