document.addEventListener("DOMContentLoaded", () => {
    const dropArea = document.getElementById("dropArea");
    const fileInput = document.getElementById("fileInput");
    const folderInput = document.getElementById("folderInput");
    const notification = document.getElementById("notification");
    const username_box=document.querySelector(".username");

    if(username_box){
        username_box.style.display='none';
    }



    showChatIdDialog();

    ["dragenter", "dragover", "dragleave", "drop"].forEach(eventName => {
        dropArea.addEventListener(eventName, (e) => {
            e.preventDefault();
            e.stopPropagation();
        }, false);
    });

    ["dragenter", "dragover"].forEach(eventName => {
        dropArea.classList.add("highlight");
    });

    ["dragleave", "drop"].forEach(eventName => {
        dropArea.classList.remove("highlight");
    });

    dropArea.addEventListener("drop", (e) => {
        const files = e.dataTransfer.files;
        fileInput.files = files;
        showNotification(files.length);
        console.log("Dropped files:", files);
    });

    fileInput.addEventListener("change", () => {
        showNotification(fileInput.files.length);
    });

    folderInput.addEventListener("change", () => {
        showNotification(folderInput.files.length);
    });
});

function showUploadDialog() {
    const modal = document.getElementById("uploadModal");
    modal.style.display = "flex";
}

function hideUploadDialog() {
    const modal = document.getElementById("uploadModal");
    modal.style.display = "none";
}

function showChatIdDialog() {
    const modal = document.getElementById("chatIdModal");
    if (modal) modal.style.display = "flex";
}

function hideChatIdDialog() {
    const modal = document.getElementById("chatIdModal");
    if (modal) modal.style.display = "none";
}

function submitChatId() {
    const name = document.getElementById("nameInput").value.trim();
    const chatId = document.getElementById("chatIdInput").value.trim();

    if (!name || !chatId) {
        alert("Please enter both name and chat ID.");
        return;
    }

    const usernameBox = document.querySelector(".username");
    const usernameText = usernameBox.querySelector("span");

    if (usernameBox && usernameText) {
        usernameText.textContent = "hey "+name;
        usernameBox.style.display = "flex";  // Show username once user submits
    }

    console.log("Name:", name, "Chat ID:", chatId);
    hideChatIdDialog();
}

function showNotification(count) {
    const notification = document.getElementById("notification");
    notification.textContent = `${count} files uploaded`;
}

let currentSlide = 0;
const totalSlides = 3;

function showInfoCarousel() {
    const carousel = document.getElementById("infoCarousel");
    carousel.style.display = "flex";
    showSlide(0); // Always start from the first slide
}

function hideInfoCarousel() {
    const carousel = document.getElementById("infoCarousel");
    carousel.style.display = "none";
}

function showSlide(index) {
    // Hide all slides
    const slides = document.querySelectorAll(".carousel-slide");
    slides.forEach(slide => {
        slide.style.display = "none";
    });
    
    // Show the current slide
    slides[index].style.display = "block";
    
    // Update indicators
    const indicators = document.querySelectorAll(".indicator");
    indicators.forEach((indicator, i) => {
        if (i === index) {
            indicator.classList.add("active");
        } else {
            indicator.classList.remove("active");
        }
    });
    
    // Update current slide index
    currentSlide = index;
}

function prevSlide() {
    let newIndex = (currentSlide - 1 + totalSlides) % totalSlides;
    showSlide(newIndex);
}

function nextSlide() {
    let newIndex = (currentSlide + 1) % totalSlides;
    showSlide(newIndex);
}

// Initialize carousel indicators when the DOM is loaded
document.addEventListener("DOMContentLoaded", () => {
    // Other existing DOMContentLoaded code
    
    // Add click events to indicators
    document.querySelectorAll(".indicator").forEach((indicator, index) => {
        indicator.addEventListener("click", () => {
            showSlide(index);
        });
    });
});