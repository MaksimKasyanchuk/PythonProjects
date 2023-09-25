"""
    URL-Shortener project
    @creator: Maks Kasyanchuk
"""

import pyshorteners


def link_config() -> None:
    """ Configuration and shortener for the Link """
    # Variable for a long url
    long_url = input("Enter a Link to Shorten: ")

    # Make a simple check, if url starts on http/https or not
    long_url = long_url.strip() # Remove leading/trailing spaces
    if not long_url.startswith(("http://", "https://")):
        long_url = "http://" + long_url

    # Initialize the Library class to start shortening the URL, get the API key of BitLy Account
    type_shortened = pyshorteners.Shortener(api_key="a316a89cc756fee6a4cee5b03ac5a153277de9af")

    # Variable for short URL (TinyURL)
    short_url_tinyurl = type_shortened.tinyurl.short(long_url)

    # Variable for short URL (BitLy)
    short_url_bitly = type_shortened.bitly.short(long_url)

    # Output for TinyURL shorten
    print("Shortened Link TinyURL -> " + short_url_tinyurl)
    # Output for BitLy shorten
    print("Shortened Link BitLy -> " + short_url_bitly)


if __name__ == '__main__':
    link_config()
