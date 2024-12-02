
# Project Overview: HackerAI

HackerAI is an open-source project designed to analyze database activity logs and detect suspicious user behaviors, such as unusual login times or changes in messaging patterns. The goal is to provide a lightweight, AI-assisted tool for identifying potential security breaches.

---

## **Key Features**
- **Anomaly Detection**: Detects unusual login times and patterns.
- **Behavioral Analysis**: Identifies changes in user activity, such as differences in message styles or abnormal frequencies.
- **Lightweight and Scalable**: Designed to handle small to medium datasets efficiently.

---

## **Technical Architecture**
1. **Input**: 
   - A SQLite database (`example.db`) generated from a `.sql` script.
   - Contains data about users, logins, and messages.

2. **Core Modules**:
   - **`main.py`**: Entry point of the project, handling database queries and anomaly detection.
   - **`utils.py`**: (Optional) Utility functions for database management and formatting.
   - **`analysis.py`**: (Optional) Modularized functions for specific types of analysis.

3. **Output**:
   - A simple console-based report indicating:
     - Suspicious login attempts (e.g., logins outside usual hours).
     - Changes in messaging patterns.
     - Other detected anomalies.

---

## **Database Structure**
The project works with the following tables:
- **Users**: Basic user information (`id`, `username`, `email`, `date_registered`).
- **Logins**: Tracks login activity (`id`, `user_id`, `timestamp`, `ip_address`, `status`).
- **Messages**: Stores messages sent by users (`id`, `user_id`, `timestamp`, `message_text`).

---

## **How It Works**
1. **Data Preparation**:
   - Create and populate the database using the `example.sql` file.
   - Run the `sqlite3` command to generate the database.

2. **Analysis**:
   - The script queries the database to detect anomalies, such as:
     - Logins outside regular hours.
     - Patterns of failed login attempts.
     - Changes in user messaging styles.

3. **Results**:
   - Results are displayed in the console with details of the detected anomalies.

---

## **Future Enhancements**
- **Visualization**: Add graphical reports for anomalies using libraries like `matplotlib`.
- **Machine Learning Integration**: Incorporate ML models for more advanced anomaly detection.
- **API Support**: Enable real-time integration with external systems through a REST API.

---

## **Contributing**
Contributions are welcome! Here’s how you can help:
1. Fork the repository and create a feature branch.
2. Make your changes and submit a pull request.
3. Join discussions in the Issues section to propose new ideas or report bugs.

---

## **License**
HackerAI is distributed under the MIT License. Feel free to use, modify, and distribute this project in compliance with the license terms.

