# Nepal Stock Market (NEPSE) API
API for Nepal Stock Market that scraps NEPSE's website and gives data in JSON.

This program scraps the real time Nepal Stock Market listed companies datas and serves it as a JSON object.

The running instance of this program could be found on:

http://apinepse.herokuapp.com/ (scrapped from NEPSE's official website, code of this is available here in this repo)

http://nepstockapi.herokuapp.com/ (This one is more fast and has more data, scrapped from sharesansar, code of this is not available in this repo, contact me individually if you need it)

To fetch the data, you could just perform a get request to any of the above mentioned link: Eg:

 	 get(http://nepstockapi.herokuapp.com/)

To run locally, install the following python packages on your local machine:

	a. flask

	b. pandas

	c. requests

	d. bs4

	e. lxml

	f. jsonify

And finally into the folder do:

	python3 index.py

For any queries or feedback, contact on: 

  Facebook:https://www.facebook.com/nepali.zuckerberg 

  Twitter: https://twitter.com/aabiseverywhere 

  Quora: https://www.quora.com/profile/Aabishkar-Wagle 

  Gmail: aabishkar2@gmail.com
