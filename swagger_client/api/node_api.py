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


class NodeApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def node_get_entry_nodes(self, **kwargs):  # noqa: E501
        """node_get_entry_nodes  # noqa: E501

        List all known entry nodes and their multiaddrs and their eligibility state  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.node_get_entry_nodes(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: dict(str, InlineResponseMap200)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.node_get_entry_nodes_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.node_get_entry_nodes_with_http_info(**kwargs)  # noqa: E501
            return data

    def node_get_entry_nodes_with_http_info(self, **kwargs):  # noqa: E501
        """node_get_entry_nodes  # noqa: E501

        List all known entry nodes and their multiaddrs and their eligibility state  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.node_get_entry_nodes_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: dict(str, InlineResponseMap200)
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
                    " to method node_get_entry_nodes" % key
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
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['keyScheme', 'passwordScheme']  # noqa: E501

        return self.api_client.call_api(
            '/node/entryNodes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='dict(str, InlineResponseMap200)',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def node_get_info(self, **kwargs):  # noqa: E501
        """node_get_info  # noqa: E501

        Information about the HOPR Node, including any options it started with. See the schema of the response to get more information on each field.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.node_get_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse2003
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.node_get_info_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.node_get_info_with_http_info(**kwargs)  # noqa: E501
            return data

    def node_get_info_with_http_info(self, **kwargs):  # noqa: E501
        """node_get_info  # noqa: E501

        Information about the HOPR Node, including any options it started with. See the schema of the response to get more information on each field.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.node_get_info_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse2003
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
                    " to method node_get_info" % key
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
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['keyScheme', 'passwordScheme']  # noqa: E501

        return self.api_client.call_api(
            '/node/info', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2003',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def node_get_metrics(self, **kwargs):  # noqa: E501
        """node_get_metrics  # noqa: E501

        Retrieve Prometheus metrics from the running node.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.node_get_metrics(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.node_get_metrics_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.node_get_metrics_with_http_info(**kwargs)  # noqa: E501
            return data

    def node_get_metrics_with_http_info(self, **kwargs):  # noqa: E501
        """node_get_metrics  # noqa: E501

        Retrieve Prometheus metrics from the running node.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.node_get_metrics_with_http_info(async_req=True)
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
                    " to method node_get_metrics" % key
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
            ['text/plain; version=0.0.4', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['keyScheme', 'passwordScheme']  # noqa: E501

        return self.api_client.call_api(
            '/node/metrics', 'GET',
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

    def node_get_peers(self, **kwargs):  # noqa: E501
        """node_get_peers  # noqa: E501

        Lists information for `connected peers` and `announced peers`. Connected peers are nodes which are connected to the node while announced peers are nodes which have announced to the network. Optionally, you can pass `quality` parameter which would filter out peers with lower quality to the one specified.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.node_get_peers(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float quality: When quality is passed, the response will only include peers with higher or equal quality to the one specified.
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.node_get_peers_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.node_get_peers_with_http_info(**kwargs)  # noqa: E501
            return data

    def node_get_peers_with_http_info(self, **kwargs):  # noqa: E501
        """node_get_peers  # noqa: E501

        Lists information for `connected peers` and `announced peers`. Connected peers are nodes which are connected to the node while announced peers are nodes which have announced to the network. Optionally, you can pass `quality` parameter which would filter out peers with lower quality to the one specified.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.node_get_peers_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float quality: When quality is passed, the response will only include peers with higher or equal quality to the one specified.
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['quality']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method node_get_peers" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'quality' in params:
            query_params.append(('quality', params['quality']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['keyScheme', 'passwordScheme']  # noqa: E501

        return self.api_client.call_api(
            '/node/peers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2002',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def node_get_version(self, **kwargs):  # noqa: E501
        """node_get_version  # noqa: E501

        Get release version of the running node.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.node_get_version(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.node_get_version_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.node_get_version_with_http_info(**kwargs)  # noqa: E501
            return data

    def node_get_version_with_http_info(self, **kwargs):  # noqa: E501
        """node_get_version  # noqa: E501

        Get release version of the running node.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.node_get_version_with_http_info(async_req=True)
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
                    " to method node_get_version" % key
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
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['keyScheme', 'passwordScheme']  # noqa: E501

        return self.api_client.call_api(
            '/node/version', 'GET',
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

    def node_ping(self, **kwargs):  # noqa: E501
        """node_ping  # noqa: E501

        Pings another node to check its availability.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.node_ping(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NodePingBody body:
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.node_ping_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.node_ping_with_http_info(**kwargs)  # noqa: E501
            return data

    def node_ping_with_http_info(self, **kwargs):  # noqa: E501
        """node_ping  # noqa: E501

        Pings another node to check its availability.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.node_ping_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NodePingBody body:
        :return: InlineResponse2001
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
                    " to method node_ping" % key
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
            '/node/ping', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2001',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def node_stream_websocket(self, **kwargs):  # noqa: E501
        """node_stream_websocket  # noqa: E501

        This is a websocket endpoint which streams legacy hopr-admin data. Authentication (if enabled) is done via either passing an `apiToken` parameter in the url or cookie `X-Auth-Token`. Connect to the endpoint by using a WS client. No preview available. Example: `ws://127.0.0.1:3001/api/v2/node/stream/websocket/?apiToken=myApiToken`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.node_stream_websocket(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse206
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.node_stream_websocket_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.node_stream_websocket_with_http_info(**kwargs)  # noqa: E501
            return data

    def node_stream_websocket_with_http_info(self, **kwargs):  # noqa: E501
        """node_stream_websocket  # noqa: E501

        This is a websocket endpoint which streams legacy hopr-admin data. Authentication (if enabled) is done via either passing an `apiToken` parameter in the url or cookie `X-Auth-Token`. Connect to the endpoint by using a WS client. No preview available. Example: `ws://127.0.0.1:3001/api/v2/node/stream/websocket/?apiToken=myApiToken`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.node_stream_websocket_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse206
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
                    " to method node_stream_websocket" % key
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
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['keyScheme', 'passwordScheme']  # noqa: E501

        return self.api_client.call_api(
            '/node/stream/websocket', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse206',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
