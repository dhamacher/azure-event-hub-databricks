import src.simulator.event_hub_sender as sim
import asyncio

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(sim.run(150, 20, 100))
