from userLibs.loaderTasks.loaderTask import LoaderTask


class SampleLoaderTask(LoaderTask):

    def __init__(self):
        super(self)
        print 'in sampleLoaderTask hello world'

    def on_start(self, args=None, kwargs=None):
        print "args = %s" % args

    def run(self, args=None, kwargs=None):

        self.on_start(args, kwargs)

        # >>>run method statements go here

        # run method statements should end here<<<

        # anything to be finalized should go here
        self.finalize(args, kwargs)

    def finalize(self, args=None, kwargs=None):

        print 'in finalize method of %s' % self.__class__.__name__


