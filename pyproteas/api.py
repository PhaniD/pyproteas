class APIInterface(object):

    """
    REST API interface class
    """

    def __init__(self, hostname, port, user_id, auth_token):
        self.hostname = hostname
        self.port = port
        self.user_id = user_id
        self.auth_token = auth_token

    def ibm_bluemix(self, query):
        """
        IBM bluemix/watson API

        Args:
            query (string): query string

        Returns:
            dict : json response from REST API
        """
        pass

    def google_vision_api(self, query):
        """
        Google vision REST API

        Args:
            query (string): query string

        Returns:
            dict : json response from REST API
        """
        pass
