<div>
  # scrapers-for-text-generation
  <p>
    Some scrapers created with scrapy for ML text-generation. <br>
    Text generators for each scraper is located in their respective folders under the name trainer.py <br>
    Text generation using LSTM from <a href="https://github.com/fchollet/keras/blob/master/examples/lstm_text_generation.py">https://github.com/fchollet/keras/blob/master/examples/lstm_text_generation.py</a>
  </p>

  <h2>Requirements for using scrapers:</h2>
  <ul>
    <li>
      Scrapy: (pip install scrapy)
    </li>
  </ul>

  <h2>Using scrapers:</h2>
  <p>Install scrapy:</p>
  
  ```shell
  pip install scrapy
  ```  

  <br>
  <p>Use the scrapy command to run the spider:</p>
  
  ```shell
  scrapy runspider anime_scraper.py
  ```


  <h2>Requirements for using trainers:</h2>
  <ul>
    <li>
      Tensorflow (pip install tensorflow)
    </li>
    <li>
      Keras (pip install keras)
    </li>
    <li>
      h5py (pip install h5py)
    </li>
  </ul>

  <h2>Scrapers for websites including: </h2>
  <ul>
    <li>
      <a href="https://myanimelist.net/">MyAnimeList</a> (gets the names of all animes)
    </li>
    <li>
      <a href="https://www.gamefaqs.com/">GameFaqs</a> (gets the names of all games for most consoles on the page <a href="https://www.gamefaqs.com/games/systems">https://www.gamefaqs.com/games/systems</a>)
    </li>
  </ul>
</div>
    
