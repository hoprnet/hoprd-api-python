# coding: utf-8

"""
    HOPRd Rest API v2

    This Rest API enables developers to interact with a hoprd node programatically.  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: tech@hoprnet.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class MessagesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def message_sign(self, **kwargs):  # noqa: E501
        """message_sign  # noqa: E501

        Signs a message given using the node’s private key. Prefixes messsage with “HOPR Signed Message: ” before signing.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.message_sign(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MessageSignBody body:
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.message_sign_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.message_sign_with_http_info(**kwargs)  # noqa: E501
            return data

    def message_sign_with_http_info(self, **kwargs):  # noqa: E501
        """message_sign  # noqa: E501

        Signs a message given using the node’s private key. Prefixes messsage with “HOPR Signed Message: ” before signing.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.message_sign_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MessageSignBody body:
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method message_sign" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['keyScheme', 'passwordScheme']  # noqa: E501

        return self.api_client.call_api(
            '/message/sign', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2004',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def messages_send_message(self, **kwargs):  # noqa: E501
        """messages_send_message  # noqa: E501

        Send a message to another peer using a given path (list of node addresses that should relay our message through network). If no path is given, HOPR will attempt to find a path.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.messages_send_message(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MessagesBody body:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.messages_send_message_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.messages_send_message_with_http_info(**kwargs)  # noqa: E501
            return data

    def messages_send_message_with_http_info(self, **kwargs):  # noqa: E501
        """messages_send_message  # noqa: E501

        Send a message to another peer using a given path (list of node addresses that should relay our message through network). If no path is given, HOPR will attempt to find a path.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.messages_send_message_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MessagesBody body:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method messages_send_message" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['keyScheme', 'passwordScheme']  # noqa: E501

        return self.api_client.call_api(
            '/messages/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def messages_sign(self, **kwargs):  # noqa: E501
        """messages_sign  # noqa: E501

        Signs a message given using the node’s private key. Prefixes messsage with “HOPR Signed Message: ” before signing.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.messages_sign(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MessagesSignBody body:
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.messages_sign_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.messages_sign_with_http_info(**kwargs)  # noqa: E501
            return data

    def messages_sign_with_http_info(self, **kwargs):  # noqa: E501
        """messages_sign  # noqa: E501

        Signs a message given using the node’s private key. Prefixes messsage with “HOPR Signed Message: ” before signing.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.messages_sign_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MessagesSignBody body:
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method messages_sign" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['keyScheme', 'passwordScheme']  # noqa: E501

        return self.api_client.call_api(
            '/messages/sign', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2004',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def messages_websocket(self, **kwargs):  # noqa: E501
        """messages_websocket  # noqa: E501

        This is a websocket endpoint which exposes a subset of message functions. Incoming messages from other nodes are sent to the websocket client in stringified Uint8Array instance of rlp-encoded data. A client may also send message by sending the following data:   { cmd: \"sendmsg\", args: { recipient: \"SOME_PEER_ID\", path: [], hops: 1} } The command arguments follow the same semantics as in the dedicated API endpoint for sending messages.  Authentication (if enabled) is done via either passing an `apiToken` parameter in the url or cookie `X-Auth-Token`. Connect to the endpoint by using a WS client. No preview available. Example: `ws://127.0.0.1:3001/api/v2/messages/websocket/?apiToken=myApiToken`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.messages_websocket(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.messages_websocket_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.messages_websocket_with_http_info(**kwargs)  # noqa: E501
            return data

    def messages_websocket_with_http_info(self, **kwargs):  # noqa: E501
        """messages_websocket  # noqa: E501

        This is a websocket endpoint which exposes a subset of message functions. Incoming messages from other nodes are sent to the websocket client in stringified Uint8Array instance of rlp-encoded data. A client may also send message by sending the following data:   { cmd: \"sendmsg\", args: { recipient: \"SOME_PEER_ID\", path: [], hops: 1} } The command arguments follow the same semantics as in the dedicated API endpoint for sending messages.  Authentication (if enabled) is done via either passing an `apiToken` parameter in the url or cookie `X-Auth-Token`. Connect to the endpoint by using a WS client. No preview available. Example: `ws://127.0.0.1:3001/api/v2/messages/websocket/?apiToken=myApiToken`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.messages_websocket_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method messages_websocket" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/text', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['keyScheme', 'passwordScheme']  # noqa: E501

        return self.api_client.call_api(
            '/messages/websocket', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
