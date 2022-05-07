/* tslint:disable */
/* eslint-disable */
/**
/* This file was automatically generated from pydantic models by running pydantic2ts.
/* Do not modify it by hand - just update the pydantic models and then re-run the script
*/

export interface AuthToken {
  access_token: string;
  refresh_token: string;
  expires_in: number;
  scope: string;
}
export interface Channel {
  id: string;
  type: number;
  guild_id: string;
  position: number;
  permission_overwrites: unknown[];
  name: string;
  topic?: string;
  nsfw?: boolean;
  last_message_id?: string;
  bitrate?: number;
  user_limit?: number;
  rate_limit_per_user?: number;
  recipients?: User[];
  icon?: string;
  owner_id?: string;
  application_id?: string;
  parent_id?: string;
  last_pin_timestamp?: string;
  rtc_region?: string;
  message_count?: number;
  member_count?: number;
  flags: number;
}
export interface User {
  id: string;
  username: string;
  discriminator: string;
  avatar: string;
  bot?: boolean;
  system?: boolean;
  mfa_enabled?: boolean;
  banner?: string;
  accent_color?: number;
  locale?: string;
}
export interface Emoji {
  id: string;
  name?: string;
  roles: Role[];
  user?: User;
  require_color?: boolean;
  managed: boolean;
  animated: boolean;
  available: boolean;
}
export interface Role {
  id: string;
  name: string;
  color: number;
  hoist: boolean;
  position: number;
  permissions: string;
  managed: boolean;
  mentionable: boolean;
}
export interface Guild {
  id: string;
  name: string;
  icon?: string;
  splash?: string;
  owner?: boolean;
  owner_id?: string;
  permissions?: string;
  region?: string;
  afk_channel_id?: string;
  afk_timeout?: number;
  widget_enabled?: boolean;
  widget_channel_id?: string;
  verification_level?: number;
  default_message_notifications?: number;
  explicit_content_filter?: number;
  roles?: Role[];
  emojis?: Emoji[];
  features: string[];
  mfa_level?: number;
  application_id?: string;
  system_channel_id?: number;
  rules_channel_id?: string;
  joined_at?: string;
  large?: boolean;
  unavailable?: boolean;
  member_count?: number;
  members?: Member[];
  channels?: Channel[];
  threads?: Channel[];
  presences?: unknown[];
  max_presences?: number;
  max_members?: number;
  vanity_url_code?: string;
  description?: string;
  banner?: string;
  premium_tier?: number;
  premium_subscription_count?: number;
  preferred_locale?: string;
  public_updates_channel_id?: string;
  max_video_channel_users?: number;
  approximate_member_count?: number;
  approximate_presence_count?: number;
  nsfw_level?: number;
}
export interface Member {
  user: User;
  nick?: string;
  avatar?: string;
  roles: Role[] | string[];
  joined_at: string;
  premium_since?: string;
  deaf: boolean;
  mute: boolean;
  pending: boolean;
  permissions?: string;
}
