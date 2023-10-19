# Scraping YouTube Comments

Scraping comments from YouTube involves extracting and collecting user comments from videos on the platform. This data retrieval process can provide valuable insights, such as understanding user sentiment, identifying popular topics, or even tracking engagement trends within specific video content. 

Once we've retrieved YouTube comments, we can leverage this data for various purposes. For instance, we can perform sentiment analysis to gauge how viewers feel about a particular video or its content. It's also useful for market research, helping us identify trends or discussions related to specific products or services. Content creators can gain feedback and user insights to refine their videos and engage with their audience more effectively. Moreover, data scientists and researchers can use this information to study online discourse, social trends, and even detect potential issues like hate speech or misinformation.

In summary, scraping YouTube comments is a valuable source of data that can be harnessed for a wide range of applications, from content improvement to market research and societal analysis.

## Installing libraries
Install the below libraries using python packet manager 'pip': 
```
!pip install google-api-python-client
!pip install pandas
```
## Generating YouTube API key
**To get your YT API key :**

1. Enable the YouTube Data API v3.
2. Create a credential
3. Restrict your API key.

*1. To enable the YouTube Data API v3:*

* Go to the Google Developers Console.
* Click the hamburger menu in the top left corner.
* Select APIs & Services.
* Click Library.
* Search for "YouTube Data API v3".
* Click Enable next to the YouTube Data API v3.

*2. To create a credential:*

* Go to the Google Developers Console.
* Click the hamburger menu in the top left corner.
* Select Credentials.
* Click Create Credentials.
* Select API Key.
* Click Create.
* Copy your API key and store it in a safe place.

*3. To restrict your API key:*

* Go to the Google Developers Console.
* Click the hamburger menu in the top left corner.
* Select Credentials.
* Click the API key you want to restrict.
* Click Restrictions.
* Under IP addresses, specify which IP addresses are allowed to access your API key.
* Under API calls, specify which API calls are allowed.
* Click Save.
  
***Once you have enabled the YouTube Data API v3, created a credential, and restricted your API key, you can start using it to make API calls to YouTube.***

## Retreiving YouTube Channel IDs
To retrieve the YT Channel ID either from Channel name or handle : [streamweasels](https://www.streamweasels.com/tools/youtube-channel-id-and-user-id-convertor/) 

## Visualizing JSON Object
After your request, to visualize the returned JSON object : [jsonformatter](https://jsonformatter.curiousconcept.com/#)

***Refer the documentation for more information : [YouTubeDocs](https://developers.google.com/youtube/v3/docs)***
