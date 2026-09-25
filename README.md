# 🛒 Smart E-Commerce Platform with Gemini AI Assistant

A modern, full-featured E-Commerce Web Application built with **Django 6.1** and powered by **Google Gemini AI**. The application features an interactive shopping assistant, full product catalog management, user order tracking, and an intuitive user interface.

---

## ✨ Key Features & Walkthrough

### 🔐 1. Authentication System
- User registration and login interface with secure password handling[cite: 12].
- Session persistence and customized greeting messages for logged-in users[cite: 5, 12].

### 🏬 2. Store Front & Dynamic Recommendations
- **Categorized Browsing**: Filter products by categories like *Electronics, Fashion, Mobiles, Jewelry, Toys, Home, Laptops*.
- **Live Product Search**: Search bar to query items instantly[cite: 5, 11].
- **Recommended For You**: Dedicated dynamic recommendation section highlighting top-selling items[cite: 5].
- **Product Details Page**: View product images, pricing in EGP, full descriptions, specifications, and instant "Add to Cart" functionality[cite: 6, 7].

### 🛒 3. Cart & Order Management
- Dynamic shopping cart counter in the header[cite: 5, 11].
- Real-time cart overview with item quantities and total price calculation[cite: 10].
- Order confirmation page with status feedback ("Order Placed Successfully!")[cite: 8].
- **My Order History**: Detailed order history page displaying previous orders, status badges (*PENDING*), items breakdown, and total order costs[cite: 9].

### 🤖 4. Smart AI Assistant (Gemini API)
- Floating **AI Assistant** widget accessible throughout the shopping journey[cite: 5, 6, 11].
- Context-aware responses powered by `gemini-2.5-flash` to query inventory and suggest products[cite: 11].
- Integrated **Strict Search Fallback** logic to handle brand-specific queries and prevent brand confusion.

---

## 📸 Application Screenshots

| Feature | Screenshot |
| :--- | :--- |
| **Authentication** | Sign-In page with feedback alerts[cite: 12] |
| **Storefront & Catalog** | Categorized browsing & dynamic recommendation banner[cite: 5] |
| **Product Detail Page** | Full specifications, price, and direct cart actions[cite: 7] |
| **Order History** | Order tracking panel with status updates[cite: 9] |
| **AI Assistant Interface** | Floating AI widget recommending matching inventory items[cite: 5, 11] |

---

## 🛠️ Tech Stack

- **Backend Framework:** Python 3.x / Django 6.1
- **Database:** SQLite3
- **AI Integration:** Google Gemini API (`google-genai` SDK / `gemini-2.5-flash` model)
- **Frontend UI:** HTML5, CSS3, JavaScript (Fetch API / AJAX)

---

## 🚀 Local Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/django-ecommerce-ai.git](https://github.com/YOUR_USERNAME/django-ecommerce-ai.git)
   cd django-ecommerce-ai