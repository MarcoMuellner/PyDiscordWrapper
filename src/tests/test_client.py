import os

import pytest

from pyddiscordwrapper import Client, User, Guild, Channel, Role, Member


def test_auth():
    client_id = 15616584861681
    scope = ['identify', 'guilds']
    redirect_uri = 'http://localhost:3000'
    url = Client.auth(client_id, scope, redirect_uri)
    assert url == 'https://discordapp.com/api/oauth2/authorize?client_id=15616584861681&scope=identify%20guilds&redirect_uri=http://localhost:3000'


def test_current_user():
    auth_token = os.getenv('AUTH_TOKEN')
    client = Client(auth_token)
    user = client.getCurrentUser(True)
    assert isinstance(user, User)


def test_current_user_guilds():
    auth_token = os.getenv('AUTH_TOKEN')
    client = Client(auth_token)
    guilds = client.getCurrentUserGuilds(True)
    assert isinstance(guilds, list)
    assert isinstance(guilds[0], Guild)


def test_get_guild():
    auth_token = os.getenv('AUTH_TOKEN')
    client = Client(auth_token)
    guilds = client.getCurrentUserGuilds(True)
    guild = client.getGuild(guilds[0].id, True)
    assert isinstance(guild, Guild)


def test_get_guild_channels():
    auth_token = os.getenv('AUTH_TOKEN')
    client = Client(auth_token)
    guilds = client.getCurrentUserGuilds(True)
    channels = client.getGuildChannels(guilds[0].id, True)
    assert isinstance(channels, list)
    assert isinstance(channels[0], Channel)


def test_get_guild_roles():
    auth_token = os.getenv('AUTH_TOKEN')
    client = Client(auth_token)
    guilds = client.getCurrentUserGuilds(True)
    roles = client.getGuildRoles(guilds[0].id, True)
    assert isinstance(roles, list)
    assert isinstance(roles[0], Role)


def test_get_guild_members():
    auth_token = os.getenv('AUTH_TOKEN')
    client = Client(auth_token)
    guilds = client.getCurrentUserGuilds(True)
    members = client.getGuildMembers(guilds[0].id, True)
    assert isinstance(members, list)
    assert isinstance(members[0], Member)
