Images scraped from the Berkeley Meme Page of Facebook on April 3, 2018

Scraped a total of 10792 images.

	- Each folder titled "imglinks_and_info_[IMGRANGE]_withname" contains 100 images (except the last folder)
	- Each image in a folder is titled "UCB[IMGRANGE]_[IMAGENUMBER]"
	- Each folder contains a CSV file, "imglinks_and_info_[IMGRANGE]_withname.csv" that holds info such as:
		- The link to the original post on the Berkeley Meme Page
		- The link to the image 
		- The number of likes, comments, and shares per image
		- The names corresponding to images in the folder
	- The two Python files are used to scrape the image data


Here is the Javascript code used to extract links to the original posts on the Berkeley Meme Page.

// recursively scroll all the way to the bottom of the page, lazy loading images
function delayandscroll() {
	window.scrollTo(0,document.body.scrollHeight);
  	setTimeout(delayandscroll, 1000);
}

// download all the links to images 
function getpostlinks() {
	for(var i = 0; i < NUMBER_OF_IMAGES; i++){
		img_urls.push(document.getElementsByTagName("td")[i].getElementsByTagName("a")[0].href)
	}
}		



HOW TO SCRAPE:
	- First create a directory where everything will be saved
	- Go into the directory and copy this README.txt as well as "img_link_scraper.py" and "img_downloader.py"
	- Now navigate to the Photos page on any Facebook page you want to scrape
	- Open up the developer console and run "delayandscroll()", this will recursively
		scroll to the bottom of the Photos page until every photo is visible
	- Create a global variable by typing: "img_urls = []" into the console
	- Run "getpostlinks()"
	- Run "copy(img_urls)" to copy img_urls to your clipboard
	- Now create a file titled "links_to_posts.txt" and paste in what you just copied 
	- Run the link scraping python script like so: "Python3 img_link_scraper.py" 
	- Run the image downloading python script like so: "Python3 img_downloader.py"
	- If everything ran smoothly you should have a directory of folders of 100 images each!