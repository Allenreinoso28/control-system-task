import asyncio
import websockets
import pygame

async def send_inputs(websocket, path):
    pygame.init()
    pygame.joystick.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    while True:
        pygame.event.pump()
        axes = [joystick.get_axis(i) for i in range(joystick.get_numaxes())]
        await websocket.send(str(axes))
        await asyncio.sleep(0.1)

start_server = websockets.serve(send_inputs, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
