// Copyright 2019 Polyaxon, Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Code generated by go-swagger; DO NOT EDIT.

package dashboards_v1

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"fmt"
	"io"

	"github.com/go-openapi/runtime"

	strfmt "github.com/go-openapi/strfmt"

	service_model "github.com/polyaxon/polyaxon/sdks/go/http_client/v1/service_model"
)

// ListDashboardsReader is a Reader for the ListDashboards structure.
type ListDashboardsReader struct {
	formats strfmt.Registry
}

// ReadResponse reads a server response into the received o.
func (o *ListDashboardsReader) ReadResponse(response runtime.ClientResponse, consumer runtime.Consumer) (interface{}, error) {
	switch response.Code() {
	case 200:
		result := NewListDashboardsOK()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return result, nil
	case 204:
		result := NewListDashboardsNoContent()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return result, nil
	case 403:
		result := NewListDashboardsForbidden()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 404:
		result := NewListDashboardsNotFound()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result

	default:
		return nil, runtime.NewAPIError("unknown error", response, response.Code())
	}
}

// NewListDashboardsOK creates a ListDashboardsOK with default headers values
func NewListDashboardsOK() *ListDashboardsOK {
	return &ListDashboardsOK{}
}

/*ListDashboardsOK handles this case with default header values.

A successful response.
*/
type ListDashboardsOK struct {
	Payload *service_model.V1ListDashboardsResponse
}

func (o *ListDashboardsOK) Error() string {
	return fmt.Sprintf("[GET /api/v1/orgs/{owner}/dashboards][%d] listDashboardsOK  %+v", 200, o.Payload)
}

func (o *ListDashboardsOK) GetPayload() *service_model.V1ListDashboardsResponse {
	return o.Payload
}

func (o *ListDashboardsOK) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	o.Payload = new(service_model.V1ListDashboardsResponse)

	// response payload
	if err := consumer.Consume(response.Body(), o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}

// NewListDashboardsNoContent creates a ListDashboardsNoContent with default headers values
func NewListDashboardsNoContent() *ListDashboardsNoContent {
	return &ListDashboardsNoContent{}
}

/*ListDashboardsNoContent handles this case with default header values.

No content.
*/
type ListDashboardsNoContent struct {
	Payload interface{}
}

func (o *ListDashboardsNoContent) Error() string {
	return fmt.Sprintf("[GET /api/v1/orgs/{owner}/dashboards][%d] listDashboardsNoContent  %+v", 204, o.Payload)
}

func (o *ListDashboardsNoContent) GetPayload() interface{} {
	return o.Payload
}

func (o *ListDashboardsNoContent) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	// response payload
	if err := consumer.Consume(response.Body(), &o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}

// NewListDashboardsForbidden creates a ListDashboardsForbidden with default headers values
func NewListDashboardsForbidden() *ListDashboardsForbidden {
	return &ListDashboardsForbidden{}
}

/*ListDashboardsForbidden handles this case with default header values.

You don't have permission to access the resource.
*/
type ListDashboardsForbidden struct {
	Payload interface{}
}

func (o *ListDashboardsForbidden) Error() string {
	return fmt.Sprintf("[GET /api/v1/orgs/{owner}/dashboards][%d] listDashboardsForbidden  %+v", 403, o.Payload)
}

func (o *ListDashboardsForbidden) GetPayload() interface{} {
	return o.Payload
}

func (o *ListDashboardsForbidden) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	// response payload
	if err := consumer.Consume(response.Body(), &o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}

// NewListDashboardsNotFound creates a ListDashboardsNotFound with default headers values
func NewListDashboardsNotFound() *ListDashboardsNotFound {
	return &ListDashboardsNotFound{}
}

/*ListDashboardsNotFound handles this case with default header values.

Resource does not exist.
*/
type ListDashboardsNotFound struct {
	Payload interface{}
}

func (o *ListDashboardsNotFound) Error() string {
	return fmt.Sprintf("[GET /api/v1/orgs/{owner}/dashboards][%d] listDashboardsNotFound  %+v", 404, o.Payload)
}

func (o *ListDashboardsNotFound) GetPayload() interface{} {
	return o.Payload
}

func (o *ListDashboardsNotFound) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	// response payload
	if err := consumer.Consume(response.Body(), &o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}