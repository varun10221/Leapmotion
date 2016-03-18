static void main(String args[])
{
	 Connect("ws://127.0.0.1:8888").Wait();
}
public static async Task Connect(String uri)
{     
     try
     {
       ClientWebSocket webSocket=new ClientWebSocket();
       webSocket.ConnectAsync(new Uri(uri),CancellationToken.None);
       await Task.WhenAll(Recieve(webSocket));
     }
     catch ( Exception ex)
     {
        Console.WriteLine("Exception: {0}",ex);
     }
     finally
     {
     	 if(webSocket!=NULL)
     	    webSocket.dispose();
     }



}

public static async Task Recieve(ClientWebSocket webSocket)
{
	  byte[] buffer= new byte[1024];
	  while(webSocket.State == WebSocketState.Open)
	  {
	  	  var result= await webSocket.RecieveAsync(new ArraySegment<byte>(buffer),CancellationToken.None);
	  	  if( result.MessageType == WebSocketMessageType.Close)
	  	  {
	  	  	 await webSocket.CloseAsync(WebSocketCloseStatus.NormalClosure,string empty,CancellationToken.None);
	  	  }
	  	  else
	  	  
	  }
}