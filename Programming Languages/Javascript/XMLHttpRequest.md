---
title: XMLHttpRequest
created: '2020-10-01T04:29:45.254Z'
modified: '2020-10-01T04:58:22.736Z'
---

# XMLHttpRequest

XMLHttpRequest (XHR) objects are used to interact with servers. You can retrieve data from a URL without having to do a full page refresh. This enables a Web page to update just part of a page without disrupting what the user is doing. XMLHttpRequest is used heavily in AJAX programming.


### Declaration:

`var xhr = new XMLHttpRequest();`

### Pointing to URL:
**Arguments:**
xhr.open("HTTP Verb", "Destination page", Asynchronous true/false)

#### GET Requests
`xhr.open("GET", "/page/anything",true);`
#### POST Requests
```
xhr.open("POST","/page/anything",true);
```
### Sending request
#### GET Request
`xhr.send();`
#### POST Request
`xhr.send("POST Data");`

### Handling response
```
xhr.onload = handleResponse; //before sending the request

function handleResponse(){
  //DO STUFF WITH THE RESPONSE. 'this' will hold the response in its properties
}
```

## Properties

- **XMLHttpRequest.response**
Returns an ArrayBuffer, Blob, Document, JavaScript object, or a DOMString, depending on the value of XMLHttpRequest.responseType, that contains the response entity body.

- **XMLHttpRequest.responseText**
Returns a DOMString that contains the response to the request as text, or null if the request was unsuccessful or has not yet been sent.

- **XMLHttpRequest.status**
Returns an unsigned short with the status of the response of the request.

- **XMLHttpRequest.statusText**
Returns a DOMString containing the response string returned by the HTTP server. Unlike XMLHttpRequest.status, this includes the entire text of the response message ("200 OK", for example). 

- **XMLHttpRequestEventTarget.ontimeout**
Is an EventHandler that is called whenever the request times out.

- **XMLHttpRequest.onload**
Is an EventHandler that is called when a response is received.

- **XMLHttpRequest.onerror**
Is an EventHandler that is called when there is an error.

## Functions

- **XMLHttpRequest.getAllResponseHeaders()**
Returns all the response headers, separated by CRLF, as a string, or null if no response has been received.

- **XMLHttpRequest.getResponseHeader()**
Returns the string containing the text of the specified header, or null if either the response has not yet been received or the header doesn't exist in the response.

- **XMLHttpRequest.open()**
Initializes a request.

- **XMLHttpRequest.send()**
Sends the request. If the request is asynchronous (which is the default), this method returns as soon as the request is sent.

- **XMLHttpRequest.setRequestHeader()**
Sets the value of an HTTP request header. You must call setRequestHeader()after open(), but before send().
