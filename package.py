from Jumpscale import j

class Package(j.baseclasses.threebot_package):

    def start(self):
        server = self.openresty
        server.configure()
        for port in [80, 443]:
            website = server.get_from_port(port)
            website.domain = "www.threefold.love"
            locations = website.locations.get(f"threefold_love_locations_{port}")

            website_location = locations.locations_static.new()
            website_location.name = "threefold_love_website"
            website_location.path_url = "/"
            fullpath = j.sal.fs.joinPaths(self.package_root, "html/")
            website_location.path_location = fullpath

            locations.configure()
            website.configure()
            website.save()

