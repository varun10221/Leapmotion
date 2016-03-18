using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net.WebSockets;
using System.Threading;
using System.Web;

namespace ConsoleApplication1
{
    class Program
    {
        public static void Main(string[] args)
        {
            Connect("ws://127.0.0.1:8888").Wait();
        }
        public static async Task Connect(string uri)
        {
            ClientWebSocket webSocket = null;
            try
            {
                webSocket = new ClientWebSocket();
                await webSocket.ConnectAsync(new Uri(uri), CancellationToken.None);
                await Task.WhenAll(Recieve(webSocket));
            }
            catch (Exception ex)
            {
                Console.WriteLine("Exception: {0}", ex);
            }
            finally
            {
                if (webSocket != null)
                    webSocket.Dispose();
            }



        }

        public static async Task Recieve(ClientWebSocket webSocket)
        {
            byte[] buffer = new byte[1024];
            while (webSocket.State == WebSocketState.Open)
            {
                var result = await webSocket.ReceiveAsync(new ArraySegment<byte>(buffer), CancellationToken.None);
                string strdata = Encoding.UTF8.GetString(buffer).TrimEnd('\0');
                string[] words = strdata.Split('}');
                string json = words[0] + '}';
                Console.WriteLine("Receive: " + json);
                Object decoded = Dec
                if (result.MessageType == WebSocketMessageType.Close)
                {
                    await webSocket.CloseAsync(WebSocketCloseStatus.NormalClosure, string.Empty, CancellationToken.None);
                }

            }
        }
    }
}
