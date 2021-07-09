<h1>Client CLI</h1>

<a href="https://github.com/hershyz/hamoc-tools/releases/tag/release-v0.1"><img src="https://raw.githubusercontent.com/hershyz/hamoc-tools/main/button.png" width="145px"></a>

<br>

<p>
  By default, the CLI makes requests to the <a href="http://hershyz.pythonanywhere.com">PythonAnywhere</a> server, but can be configured otherwise.
</p>
<pre>
  The target URI can be changed by updating the client on line 103:
  client = Hamoc_Client("http://hershyz.pythonanywhere.com") -> client = Hamoc_Client([new uri])
</pre>

<br>

<p>
  <strong>Running</strong>
  <pre>
    cd /cli
    python release_cli.py
  </pre>
  
  <strong>Commands</strong>
  <pre>
      help:                                                                 displays all available commands
      add [symbols]:                                                        adds symbols to the server target list
      getsymbols:                                                           returns a list of symbols from the target list
      del [symbols]:                                                        deletes symbols from the server target list
      updatestocks:                                                         attempts to update stock data
      updateoptions:                                                        attempts to update options data
      getstockval [symbol, YYYY-MM-DD, property]:                           returns the property of a stock given a symbol and date
      contracts [symbol, YYYY-MM-DD]:                                       returns all contracts of a given stock on a specific date
      getcontractval [symbol, contract symbol, YYYY-MM-DD, property]:       returns the property of a contract symbol given a date
      stockquery [low, high]:                                               returns all stored stocks on specific dates with a close price between low and high
      optionquery [low, high, property]:                                    returns all contract symbols with the given property between low and high
      queries:                                                              displays all queries made and their results for the current client session
  </pre>
</p>
