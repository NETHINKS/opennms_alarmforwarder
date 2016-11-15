<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <!-- CSS -->
        <link href="/static/css/bootstrap.min.css" rel="stylesheet">
        <link href="/static/css/alarmforwarder.css" rel="stylesheet">

        <!-- JavaScript -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
        <script src="/static/js/bootstrap.min.js"></script>

        <!-- Favicon -->
        <link rel="shortcut icon" type="image/x-icon" href="/static/images/favicon.ico" />

        <title>OpenNMS AlarmForwarder Admin</title>
    </head>

    <body>
        {% if session.username %}
            {% include 'include/navbar.html.tpl' %}
            {% include 'include/messagebar.html.tpl' %}
        {% endif %}
