from Jumpscale import j


class Package(j.baseclasses.threebot_package):
    """
    JSX> cl = j.servers.threebot.local_start_zerobot(background=False)
    JSX> cl = j.clients.gedis.get("abc", port=8901, package_name="zerobot.packagemanager")
    JSX> cl.actors.package_manager.package_add(git_url="https://github.com/threefold-love/www_threefold_love/tree/3bot")
    """
    DOMAIN = "www.threefold.love"
    def start(self):
        server = self.openresty
        server.configure()
        website_threefold_love = server.websites.get("www_threefold_love")
        website_threefold_love.domain = self.DOMAIN
        website_threefold_love.port = 80
        website_threefold_love.ssl = False

        websites = [server.get_from_port(80), server.get_from_port(443), website_3bot]
        for website in websites:
            locations = website.locations.get(f"3bot_locations_{website.name}")

            website_location = locations.locations_static.new()
            website_location.name = "threefold_love_website"
            website_location.path_url = "/" if website.domain == self.DOMAIN else "/threefold_love"
            fullpath = j.sal.fs.joinPaths(self.package_root, "html/")
            website_location.path_location = fullpath

            locations.configure()
            website.configure()
            website.save()
