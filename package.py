from Jumpscale import j

class Package(j.baseclasses.threebot_package):
    """
    to start need to run 
    kosmos -p "j.tools.threebot_packages.get('threefold_love_stag',giturl='https://github.com/threefold-love/www_threefold_love.git',branch='master')"
    kosmos -p "j.servers.threebot.default.start(web=True, ssl=False)"
    """
    def _init(self, **kwargs):
        self.branch = kwargs["package"].branch or "master"
        self.threefold_love_stag = "https://github.com/threefold-love/www_threefold_love.git"

    def prepare(self):
        """
        called when the 3bot starts
        :return:
        """
        server = self.openresty
        server.install(reset=True)
        server.configure()
        website = server.websites.get("threefold_love_stag")
        website.ssl = False
        website.port = 80
        locations = website.locations.get("threefold_love_stag")
        static_location = locations.locations_static.new()
        static_location.name = "static"
        static_location.path_url = "/"
        path = j.clients.git.getContentPathFromURLorPath(self.threefold_love_stag, branch=self.branch, pull=True)
        static_location.path_location = path
        static_location.use_jumpscale_weblibs = True
        website.path = path
        locations.configure()
        website.configure()

    def start(self):
        """
        called when the 3bot starts
        :return:
        """
        self.prepare()
    def stop(self):
        """
        called when the 3bot stops
        :return:
        """
        pass

    def uninstall(self):
        """
        called when the package is no longer needed and will be removed from the threebot
        :return:
        """
        pas
