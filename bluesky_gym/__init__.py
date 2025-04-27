from gymnasium.envs.registration import register
from .utils import *
 
def register_envs():
    """Import the envs module so that environments / scenarios register themselves."""
    register(
        id="SectorCREnv-v0",
        entry_point="CR_HiFi.bluesky_gym.envs.sector_cr_env:SectorCREnv",
        max_episode_steps=200,
    )