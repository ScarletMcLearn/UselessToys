// ==UserScript==
// @name         YouTube Video Auto-Play
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  Automatically plays YouTube videos when the page loads.
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
            if (videoPlayer.paused) {
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

    // Wait for the page to fully load
    window.addEventListener('load', () => {
        // Run the script after a slight delay to ensure the player is ready
        setTimeout(init, 1000);
    });
})();
