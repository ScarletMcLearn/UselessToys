// ==UserScript==
// @name         YouTube Video Auto-Play
// @namespace    http://tampermonkey.net/
// @version      1.2
// @description  Automatically plays YouTube videos when the page loads or when navigating to a new video, including autoplayed ones.
// @author       YourName
// @match        https://www.youtube.com/watch?v=*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    // Check if the video player is visible and ready
    function isVideoPlayerVisible() {
        const videoPlayer = document.querySelector('video');
        return videoPlayer && videoPlayer.offsetParent !== null;
    }

    // Attempt to play the video
    function playVideo() {
        const videoPlayer = document.querySelector('video');

        if (videoPlayer) {
            if (videoPlayer.paused || videoPlayer.readyState < 3) { // Ensure the video is ready to play
                // First try a click to play
                const playerContainer = document.querySelector('.html5-video-player');
                if (playerContainer) {
                    playerContainer.click();
                }

                // If clicking doesn't work, attempt programmatic play
                videoPlayer.play().catch(err => {
                    console.error('Failed to play video programmatically:', err);
                });
            }
        }
    }

    // Main logic to check and play the video
    function init() {
        if (window.location.href.includes('https://www.youtube.com/watch?v=') && isVideoPlayerVisible()) {
            playVideo();
        } else {
            console.warn('This script only works on YouTube video pages.');
        }
    }

    // Observe URL changes and autoplay triggers to handle navigation to a new video
    function observeChanges() {
        let lastUrl = window.location.href;
        const observer = new MutationObserver(() => {
            const currentUrl = window.location.href;
            if (currentUrl !== lastUrl) {
                lastUrl = currentUrl;
                setTimeout(init, 1000); // Delay to allow the new video to load
            }
        });
        observer.observe(document.body, { childList: true, subtree: true });

        // Also observe changes to the video player state
        const videoPlayer = document.querySelector('video');
        if (videoPlayer) {
            videoPlayer.addEventListener('loadeddata', () => {
                setTimeout(playVideo, 500); // Ensure playback starts after data is loaded
            });
        }
    }

    // Wait for the page to fully load
    window.addEventListener('load', () => {
        // Run the script after a slight delay to ensure the player is ready
        setTimeout(init, 1000);
        observeChanges();
    });
})();
