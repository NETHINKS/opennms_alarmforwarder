
        {% if current_path != "login" %}
            </main>
            <footer>
                <div class="container">
                    <hr />
                    <div class="row">
                        <div class="col-xs-12 col-md-6">
                            &copy; NETHINKS GmbH | <i class="fa fa-book" aria-hidden="true"></i> <a href="{{ baseurl }}/docs" target="_blank">Documentation</a> | <i class="fa fa-github" aria-hidden="true"></i> <a href="https://github.com/NETHINKS/opennms_alarmforwarder" target="_blank">GitHub Project</a>
                        </div>
                        <div class="col-xs-12 col-md-offset-4 col-md-2">
                          <a href="https://www.nethinks.com/" target="_blank"><img src="{{ baseurl }}/static/img/NEThinks_2c.svg" class="img-responsive center-block"></a>
                        </div>
                    </div>
                </div>
            </footer>
         {% endif %}
        <!-- JavaScript -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
        <script src="{{ baseurl }}/static/js/netstyle.min.js"></script>
    </body>
</html>
