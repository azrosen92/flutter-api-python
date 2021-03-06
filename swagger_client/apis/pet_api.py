# coding: utf-8

"""
    Swagger Petstore

    This is a sample server Petstore server.  You can find out more about Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).  For this sample, you can use the api key `special-key` to test the authorization filters.

    OpenAPI spec version: 1.0.6
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class PetApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def add_pet(self, body, **kwargs):
        """
        Add a new pet to the store
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_pet(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Pet body: Pet object that needs to be added to the store (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.add_pet_with_http_info(body, **kwargs)
        else:
            (data) = self.add_pet_with_http_info(body, **kwargs)
            return data

    def add_pet_with_http_info(self, body, **kwargs):
        """
        Add a new pet to the store
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_pet_with_http_info(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Pet body: Pet object that needs to be added to the store (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_pet" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_pet`")

        resource_path = '/pet'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/xml'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'application/xml'])

        # Authentication setting
        auth_settings = ['petstore_auth']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def delete_pet(self, pet_id, **kwargs):
        """
        Deletes a pet
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_pet(pet_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int pet_id: Pet id to delete (required)
        :param str api_key: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_pet_with_http_info(pet_id, **kwargs)
        else:
            (data) = self.delete_pet_with_http_info(pet_id, **kwargs)
            return data

    def delete_pet_with_http_info(self, pet_id, **kwargs):
        """
        Deletes a pet
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_pet_with_http_info(pet_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int pet_id: Pet id to delete (required)
        :param str api_key: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['pet_id', 'api_key']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_pet" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'pet_id' is set
        if ('pet_id' not in params) or (params['pet_id'] is None):
            raise ValueError("Missing the required parameter `pet_id` when calling `delete_pet`")

        resource_path = '/pet/{petId}'.replace('{format}', 'json')
        path_params = {}
        if 'pet_id' in params:
            path_params['petId'] = params['pet_id']

        query_params = {}

        header_params = {}
        if 'api_key' in params:
            header_params['api_key'] = params['api_key']

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/xml'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['petstore_auth']

        return self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def find_pets_by_status(self, status, **kwargs):
        """
        Finds Pets by status
        Multiple status values can be provided with comma separated strings

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.find_pets_by_status(status, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] status: Status values that need to be considered for filter (required)
        :return: list[Pet]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.find_pets_by_status_with_http_info(status, **kwargs)
        else:
            (data) = self.find_pets_by_status_with_http_info(status, **kwargs)
            return data

    def find_pets_by_status_with_http_info(self, status, **kwargs):
        """
        Finds Pets by status
        Multiple status values can be provided with comma separated strings

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.find_pets_by_status_with_http_info(status, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] status: Status values that need to be considered for filter (required)
        :return: list[Pet]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['status']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method find_pets_by_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'status' is set
        if ('status' not in params) or (params['status'] is None):
            raise ValueError("Missing the required parameter `status` when calling `find_pets_by_status`")

        resource_path = '/pet/findByStatus'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'status' in params:
            query_params['status'] = params['status']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/xml'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['petstore_auth']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[Pet]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def find_pets_by_tags(self, tags, **kwargs):
        """
        Finds Pets by tags
        Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.find_pets_by_tags(tags, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] tags: Tags to filter by (required)
        :return: list[Pet]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.find_pets_by_tags_with_http_info(tags, **kwargs)
        else:
            (data) = self.find_pets_by_tags_with_http_info(tags, **kwargs)
            return data

    def find_pets_by_tags_with_http_info(self, tags, **kwargs):
        """
        Finds Pets by tags
        Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.find_pets_by_tags_with_http_info(tags, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] tags: Tags to filter by (required)
        :return: list[Pet]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tags']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method find_pets_by_tags" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tags' is set
        if ('tags' not in params) or (params['tags'] is None):
            raise ValueError("Missing the required parameter `tags` when calling `find_pets_by_tags`")

        resource_path = '/pet/findByTags'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'tags' in params:
            query_params['tags'] = params['tags']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/xml'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['petstore_auth']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[Pet]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_pet_by_id(self, pet_id, **kwargs):
        """
        Find pet by ID
        Returns a single pet

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_pet_by_id(pet_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int pet_id: ID of pet to return (required)
        :return: Pet
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_pet_by_id_with_http_info(pet_id, **kwargs)
        else:
            (data) = self.get_pet_by_id_with_http_info(pet_id, **kwargs)
            return data

    def get_pet_by_id_with_http_info(self, pet_id, **kwargs):
        """
        Find pet by ID
        Returns a single pet

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_pet_by_id_with_http_info(pet_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int pet_id: ID of pet to return (required)
        :return: Pet
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['pet_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_pet_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'pet_id' is set
        if ('pet_id' not in params) or (params['pet_id'] is None):
            raise ValueError("Missing the required parameter `pet_id` when calling `get_pet_by_id`")

        resource_path = '/pet/{petId}'.replace('{format}', 'json')
        path_params = {}
        if 'pet_id' in params:
            path_params['petId'] = params['pet_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/xml'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['api_key']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Pet',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def update_pet(self, body, **kwargs):
        """
        Update an existing pet
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_pet(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Pet body: Pet object that needs to be added to the store (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_pet_with_http_info(body, **kwargs)
        else:
            (data) = self.update_pet_with_http_info(body, **kwargs)
            return data

    def update_pet_with_http_info(self, body, **kwargs):
        """
        Update an existing pet
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_pet_with_http_info(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Pet body: Pet object that needs to be added to the store (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_pet" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_pet`")

        resource_path = '/pet'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/xml'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'application/xml'])

        # Authentication setting
        auth_settings = ['petstore_auth']

        return self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def update_pet_with_form(self, pet_id, **kwargs):
        """
        Updates a pet in the store with form data
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_pet_with_form(pet_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int pet_id: ID of pet that needs to be updated (required)
        :param str name: Updated name of the pet
        :param str status: Updated status of the pet
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_pet_with_form_with_http_info(pet_id, **kwargs)
        else:
            (data) = self.update_pet_with_form_with_http_info(pet_id, **kwargs)
            return data

    def update_pet_with_form_with_http_info(self, pet_id, **kwargs):
        """
        Updates a pet in the store with form data
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_pet_with_form_with_http_info(pet_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int pet_id: ID of pet that needs to be updated (required)
        :param str name: Updated name of the pet
        :param str status: Updated status of the pet
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['pet_id', 'name', 'status']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_pet_with_form" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'pet_id' is set
        if ('pet_id' not in params) or (params['pet_id'] is None):
            raise ValueError("Missing the required parameter `pet_id` when calling `update_pet_with_form`")

        resource_path = '/pet/{petId}'.replace('{format}', 'json')
        path_params = {}
        if 'pet_id' in params:
            path_params['petId'] = params['pet_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'name' in params:
            form_params.append(('name', params['name']))
        if 'status' in params:
            form_params.append(('status', params['status']))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/xml'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = ['petstore_auth']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def upload_file(self, pet_id, **kwargs):
        """
        uploads an image
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.upload_file(pet_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int pet_id: ID of pet to update (required)
        :param str additional_metadata: Additional data to pass to server
        :param file file: file to upload
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.upload_file_with_http_info(pet_id, **kwargs)
        else:
            (data) = self.upload_file_with_http_info(pet_id, **kwargs)
            return data

    def upload_file_with_http_info(self, pet_id, **kwargs):
        """
        uploads an image
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.upload_file_with_http_info(pet_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int pet_id: ID of pet to update (required)
        :param str additional_metadata: Additional data to pass to server
        :param file file: file to upload
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['pet_id', 'additional_metadata', 'file']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upload_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'pet_id' is set
        if ('pet_id' not in params) or (params['pet_id'] is None):
            raise ValueError("Missing the required parameter `pet_id` when calling `upload_file`")

        resource_path = '/pet/{petId}/uploadImage'.replace('{format}', 'json')
        path_params = {}
        if 'pet_id' in params:
            path_params['petId'] = params['pet_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'additional_metadata' in params:
            form_params.append(('additionalMetadata', params['additional_metadata']))
        if 'file' in params:
            local_var_files['file'] = params['file']

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['multipart/form-data'])

        # Authentication setting
        auth_settings = ['petstore_auth']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ApiResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
