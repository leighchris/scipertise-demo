// replace these values with those generated in your TokBox Account
var apiKey = "46235562";
var sessionId = "1_MX40NjIzNTU2Mn5-MTU0NDYzODg5ODk2NX41WHNnTzAzNjQrZXMxdjQ3ZnpETHRHbm5-fg";
var token = "T1==cGFydG5lcl9pZD00NjIzNTU2MiZzaWc9MjU4MGE2MmVmMzc4OGZhOWZiOGEzZTE4YzdkMzA3ZmU5ZDE0OTRjODpzZXNzaW9uX2lkPTFfTVg0ME5qSXpOVFUyTW41LU1UVTBORFl6T0RnNU9EazJOWDQxV0hOblR6QXpOalFyWlhNeGRqUTNabnBFVEhSSGJtNS1mZyZjcmVhdGVfdGltZT0xNTQ0NjM4OTMwJm5vbmNlPTAuNjAzNjAxMzg2NDE1NTQ2MyZyb2xlPXB1Ymxpc2hlciZleHBpcmVfdGltZT0xNTQ0NjYwNTMwJmluaXRpYWxfbGF5b3V0X2NsYXNzX2xpc3Q9";

// (optional) add server code here
initializeSession();

// Handling all of our errors here by alerting them
function handleError(error) {
  if (error) {
    alert(error.message);
  }
}

function initializeSession() {
  var session = OT.initSession(apiKey, sessionId);

  // Subscribe to a newly created stream
    session.on('streamCreated', function(event) {
  session.subscribe(event.stream, 'subscriber', {
    insertMode: 'append',
    width: '100%',
    height: '100%'
  }, handleError);
});

  // Create a publisher
  var publisher = OT.initPublisher('publisher', {
    insertMode: 'append',
    width: '100%',
    height: '100%'
  }, handleError);

  // Connect to the session
  session.connect(token, function(error) {
    // If the connection is successful, publish to the session
    if (error) {
      handleError(error);
    } else {
      session.publish(publisher, handleError);
    }
  });
}


//// Initialize an OpenTok Session object
//var session = TB.initSession(sessionId);
//
//// Initialize a Publisher, and place it into the element with id="publisher"
//var publisher = TB.initPublisher(apiKey, 'publisher');
//
//// Attach event handlers
//session.on({
//
//  	// This function runs when session.connect() asynchronously completes
//  	sessionConnected: function(event) {
//		// Publish the publisher we initialzed earlier (this will trigger 'streamCreated' on other
//		// clients)
//		session.publish(publisher, function(){
//			screenshare();
//		});
//	},
//
//  // This function runs when another client publishes a stream (eg. session.publish())
//  streamCreated: function(event) {
//	// Create a container for a new Subscriber, assign it an id using the streamId, put it inside
//	// the element with id="subscribers"
//	var subContainer = document.createElement('div');
//	subContainer.id = 'stream-' + event.stream.streamId;
//	document.getElementById('subscribers').appendChild(subContainer);
//
//	// Subscribe to the stream that caused this event, put it inside the container we just made
//	session.subscribe(event.stream, subContainer);
//}
//
//
//});
