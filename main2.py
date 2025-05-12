# Ensure you have gallery-dl installed: pip install gallery-dl
import gallery_dl
import gallery_dl.config
import gallery_dl.job
# Import the base exception directly from gallery_dl
from gallery_dl import exception
import logging
from pprint import pprint

# Optional: Configure logging for gallery-dl to see its internal messages
# logging.basicConfig(level=logging.DEBUG)

def list_gallery_urls(url: str) -> list[str]:
    """
    Uses gallery-dl to extract a list of direct media URLs from a gallery URL.

    This function simulates the behavior of the '--list-urls' command-line option
    by configuring a DownloadJob appropriately using a config dictionary.

    Args:
        url: The URL of the gallery (e.g., an album, user profile)
             supported by gallery-dl.

    Returns:
        A list of strings, where each string is a direct URL to a media file.
        Returns an empty list if no URLs are found or if an error occurs.
    """
    extracted_urls = []
    # Store original config to restore later if needed, though clear() is usually sufficient
    # original_config = gallery_dl.config.dump()
    # try:
        # Create a configuration dictionary for gallery-dl options.
    conf_options = {
            "base-directory": "~/gallery-dl-custom/",
            "list_urls": True,      # Equivalent to --list-urls
            "download": False,      # Ensure download is off
            "write-metadata": False # Don't write metadata files
            # Add other necessary options here if needed, e.g., for authentication:
            # "cookies": "/path/to/cookies.txt",
            # "username": "your_username",
            # "password": "your_password",
        }

        # Initialize the global config (optional but good practice)
        # This loads default settings which our options will override
    gallery_dl.config.load()
    pprint(vars(gallery_dl.config))

        # Apply our specific overrides by iterating through the options
        # The key for extractor options is a tuple: ('extractor', option_name)
    for key, value in conf_options.items():
        # Revised: Pass key path components as separate arguments
        gallery_dl.config.set('extractor', key, value)


        # Create a DownloadJob instance for the given URL.
        # It reads from the global config state managed by gallery_dl.config.
    #     job = gallery_dl.job.DownloadJob(url)


    #     # The run() method returns an iterator that yields tuples.
    #     # When list-urls is True, the tuple format is typically:
    #     # (category, url, filepath)
    #     # where category might be 'urls', url is the direct media URL,
    #     # and filepath might be None or the same as url.
    #     # We are interested in the second element (the URL).
    #     for result in job.run():
    #         # The structure of the result tuple might vary slightly,
    #         # but the direct URL is usually the second element.
    #         if len(result) >= 2 and isinstance(result[1], str):
    #              # Basic check to ensure it looks like a URL
    #             if result[1].startswith(('http://', 'https://')):
    #                 extracted_urls.append(result[1])
    #         else:
    #             # Log unexpected result format if needed
    #             logging.warning(f"Unexpected result format from job.run(): {result}")

    # # Use the correctly imported exception class
    # except exception.GalleryDLException as e:
    #     # Handle specific gallery-dl errors
    #     print(f"An error occurred with gallery-dl: {e}")
    # except Exception as e:
    #     # Handle other potential errors (e.g., network issues, config errors)
    #     print(f"An unexpected error occurred: {e}")
    # finally:
    #     # Important: Reset config after use to avoid affecting subsequent calls
    #     # if running multiple jobs with different settings in the same script.
    #     gallery_dl.config.clear()
    #     # Optionally, restore original config if needed for complex scenarios
    #     # gallery_dl.config.load(original_config)


    return extracted_urls

# --- Example Usage ---
if __name__ == "__main__":
    # Example: Replace with a URL gallery-dl supports
    # Using an Imgur album URL as an example
    gallery_url = "https://everia.club/2025/04/22/akane-nishikawa-%e8%a5%bf%e5%b7%9d%e8%8c%9c-minisuka-tv-2025-04-10-regular-gallery-set-10-01/"

    print(f"Attempting to list URLs for: {gallery_url}")
    urls = list_gallery_urls(gallery_url)

    if urls:
        print("\nExtracted URLs:")
        for i, item_url in enumerate(urls):
            print(f"{i + 1}: {item_url}")
    else:
        print("\nNo URLs were extracted or an error occurred.")

    # --- Example with potential authentication (requires configuration) ---
    # reddit_url = "https://www.reddit.com/user/some_user/submitted/"
    # print(f"\nAttempting to list URLs for: {reddit_url}")
    # Note: Accessing private/NSFW Reddit content might require
    # authentication options set by iterating through gallery_dl.config.set above.
    # reddit_urls = list_gallery_urls(reddit_url)
    # if reddit_urls:
    #     print("\nExtracted Reddit URLs:")
    #     for i, item_url in enumerate(reddit_urls):
    #         print(f"{i + 1}: {item_url}")
    # else:
    #     print("\nNo Reddit URLs were extracted or an error occurred (check authentication/URL validity).")

