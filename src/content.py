import requests

class Content():
    def __init__(self, Requests, log):
        self.Requests = Requests
        self.log = log
        self.content = {}

    def get_content(self):
        self.content = self.Requests.fetch("custom", f"https://shared.{self.Requests.region}.a.pvp.net/content-service/v3/content", "get")
        return self.content

    def get_latest_season_id(self, content):
        for season in content["Seasons"]:
            if season["IsActive"]:
                self.log(f"retrieved season id: {season['ID']}")
                return season["ID"]

    def get_previous_season_id(self, content):
        previous = content["Seasons"][0]
        for season in content["Seasons"]:
            if season["IsActive"]:
                self.log(f"retrieved previous season id: {previous['ID']}")
                return previous["ID"]
            # Only store the previous act.
            if (season["Type"] == "episode"):
                continue
            previous = season
        return None

    def get_all_agents(self):
        rAgents = requests.get("https://valorant-api.com/v1/agents?isPlayableCharacter=true").json()
        agent_dict = {}
        agent_dict.update({None: None})
        agent_dict.update({"": ""})
        for agent in rAgents["data"]:
            agent_dict.update({agent['uuid'].lower(): agent['displayName']})
        self.log(f"retrieved agent dict: {agent_dict}")
        return agent_dict

    def get_all_maps(self):
        """
        Requests data and assets of all maps.
        :return: JSON of all map information.
        """
        return requests.get("https://valorant-api.com/v1/maps").json()

    def get_map_urls(self, maps) -> dict:
        map_dict = {}
        map_dict.update({None: None})
        for Vmap in maps["data"]:
            map_dict.update({Vmap['mapUrl'].lower(): Vmap['displayName']})
        self.log(f"retrieved map dict: {map_dict}")
        return map_dict

    def get_map_splashes(self, val_maps) -> dict:
        """
        Iterates through all maps, pulling map names and splash screens.
        :param val_maps: JSON of all maps.
        :return: A dictionary of maps to splashes.
        """
        val_map_dict = {}
        val_map_dict.update({None: None})
        for val_map in val_maps["data"]:
            val_map_dict.update({val_map['displayName']: val_map['splash']})
        return val_map_dict

    def get_act_episode_from_act_id(self, act_id):
        final = {
            "act": None,
            "episode": None
        }
        act_found = False
        for season in self.content["Seasons"]:
            if season["ID"].lower() == act_id.lower():
                final["act"] = int(season["Name"][-1])
                act_found = True
            if act_found and season["Type"] == "episode":
                final["episode"] = int(season["Name"][-1])
                break
        return final
