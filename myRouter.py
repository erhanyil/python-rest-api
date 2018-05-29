from RouteLibrary import RouteLibrary

router = RouteLibrary()

router.map('homeController', 'home', '/', 'home')

router.map('userController', 'getAllUsers', '/user/', 'user')
router.map('userController', 'getAllUsers', '/user/<id>', 'getUser')

router.run()


