import os

import pytest

from pydiscordwrapper import AsyncClient, User, Guild, Channel, Role, Member

@pytest.mark.asyncio
async def test_auth():
    client_id = 15616584861681
    scope = ['identify', 'guilds']
    redirect_uri = 'http://localhost:3000'
    url = AsyncClient.auth(client_id, scope, redirect_uri)
    assert url == 'https://discordapp.com/api/oauth2/authorize?client_id=15616584861681&scope=identify%20guilds&redirect_uri=http://localhost:3000'

@pytest.mark.asyncio
async def test_current_user():
    auth_token = os.getenv('AUTH_TOKEN')
    client = AsyncClient(auth_token)
    user = await client.getCurrentUser(True)
    assert isinstance(user, User)

@pytest.mark.asyncio
async def test_current_user_guilds():
    auth_token = os.getenv('AUTH_TOKEN')
    client = AsyncClient(auth_token)
    guilds = await client.getCurrentUserGuilds(True)
    assert isinstance(guilds, list)
    assert isinstance(guilds[0], Guild)

@pytest.mark.asyncio
async def test_get_guild():
    auth_token = os.getenv('AUTH_TOKEN')
    client = AsyncClient(auth_token)
    guilds = await client.getCurrentUserGuilds(True)
    guild = await client.getGuild(guilds[0].id, True)
    assert isinstance(guild, Guild)

@pytest.mark.asyncio
async def test_get_guild_channels():
    auth_token = os.getenv('AUTH_TOKEN')
    client = AsyncClient(auth_token)
    guilds = await client.getCurrentUserGuilds(True)
    channels = await client.getGuildChannels(guilds[0].id, True)
    assert isinstance(channels, list)
    assert isinstance(channels[0], Channel)

@pytest.mark.asyncio
async def test_get_guild_roles():
    auth_token = os.getenv('AUTH_TOKEN')
    client = AsyncClient(auth_token)
    guilds = await client.getCurrentUserGuilds(True)
    roles = await client.getGuildRoles(guilds[0].id, True)
    assert isinstance(roles, list)
    assert isinstance(roles[0], Role)

@pytest.mark.asyncio
async def test_get_guild_members():
    auth_token = os.getenv('AUTH_TOKEN')
    client = AsyncClient(auth_token)
    guilds = await client.getCurrentUserGuilds(True)
    members = await client.getGuildMembers(guilds[0].id, True)
    assert isinstance(members, list)
    assert isinstance(members[0], Member)
