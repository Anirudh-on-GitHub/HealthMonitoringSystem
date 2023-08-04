<!DOCTYPE html>
<html>
<head>
    <h1>Health Data Portal - README</h1>
</head>
<body>
    <h1>Description:</h1>
    <p>Health Data Portal is a Django web application that allows users to access and retrieve patient information stored in a CSV file. Users can enter a patient ID to view specific details such as name, age, heart rate, blood pressure, and temperature for the corresponding patient.</p>
    <h1>Contents:</h1>
    <ol>
        <li>
            <h2>Requirements:</h2>
            <ul>
                <li>Python</li>
                <li>Django</li>
            </ul>
        </li>
        <li>
            <h2>Installation:</h2>
            <p>Clone this repository to your local machine using the following command:</p>
            <pre><code>git clone &lt;repository_url&gt;</code></pre>
            <p>Install the required dependencies using pip:</p>
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li>
            <h2>Usage:</h2>
            <p>Run the Django development server:</p>
            <pre><code>python manage.py runserver</code></pre>
            <p>Access the Health Data Portal by navigating to <a href="http://localhost:8000/">http://localhost:8000/</a> in your web browser.</p>
        </li>
        <li>
            <h2>Patient Data:</h2>
            <p>The patient data is stored in a CSV file located at <code>static/patient.csv</code>.</p>
            <p>The CSV file contains the following columns:</p>
            <ul>
                <li>PatientID</li>
                <li>Name</li>
                <li>Age</li>
                <li>HeartRate</li>
                <li>BloodPressure</li>
                <li>Temperature</li>
            </ul>
        </li>
        <li>
            <h2>Web Pages:</h2>
            <ul>
                <li>
                    <h3>Home Page:</h3>
                    <p>The home page allows users to enter a patient ID through a form and submit the request.</p>
                    <p>URL: <a href="http://localhost:8000/">http://localhost:8000/</a></p>
                </li>
                <li>
                    <h3>Patient Information Page:</h3>
                    <p>After submitting the patient ID, the corresponding patient's information will be displayed in a tabular format on this page.</p>
                    <p>URL: <a href="http://localhost:8000/display_data">http://localhost:8000/display_data</a></p>
                </li>
            </ul>
        </li>
        <li>
            <h2>Example:</h2>
            <p>To illustrate how the application works, consider the following example:</p>
            <ul>
                <li>Input patient ID: <code>1</code></li>
                <li>The corresponding patient information will be displayed, as shown below:</li>
            </ul>
            <table>
                <tr>
                    <th>Patient ID</th>
                    <th>Name</th>
                    <th>Age</th>
                    <th>Heart Rate</th>
                    <th>Blood Pressure</th>
                    <th>Temperature</th>
                </tr>
                <tr>
                    <td>1</td>
                    <td>Aarav Patel</td>
                    <td>38</td>
                    <td>78</td>
                    <td>120/80</td>
                    <td>98.6</td>
                </tr>
            </table>
        </li>
        <li>
            <h2>Contributing:</h2>
            <p>Contributions to this project are welcome! If you find any issues or have ideas to improve the application, feel free to open an issue or submit a pull request.</p>
        </li>
        <li>
            <h2>License:</h2>
            <p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for more details.</p>
        </li>
    </ol>
</body>
</html>
