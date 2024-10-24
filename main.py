from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from config import mycollection as mc
from model import event 


app = FastAPI()

subcribers = {}

@app.websocket("/Subcribe_task_bids/{taskId}")
async def websocket_endpoint(websocket: WebSocket, taskId : int):
    try:
        subcribers[taskId] = websocket
        await websocket.accept()
        await websocket.send_json({"message": "Connected successfully!"})
        while True:
            data = await websocket.receive_text()
    
    except WebSocketDisconnect:
        del subcribers[taskId]



@app.post("/sendEvent/{task_id}")
async def eventHandler(task_id : int):

    updated_data = mc.find_one({"task_id": task_id})

    latest_bid = updated_data["task_bids"][-1]

    print(latest_bid[-1])

    for connection in subcribers:
        if connection == event.task_id:
            websocket = subcribers[connection]
            await websocket.send_json(latest_bid)
            return {"message" : "event received published succesfully"}

        else:
            # Handle the case where the client is disconnected
            print(f"Client {event.task_id} is not connected.")
            return {"message" : "event received but not published"}


@app.get("/")
async def root():
    return {"message": "Hello World"}