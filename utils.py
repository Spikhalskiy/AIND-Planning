class _CaptureEq:
    'Object wrapper that remembers "other" for successful equality tests.'
    def __init__(self, obj):
        self.obj = obj
        self.match = obj
    def __eq__(self, other):
        result = (self.obj == other)
        if result:
            self.match = other
        return result
    def __getattr__(self, name):  # support hash() or anything else needed by __contains__
        return getattr(self.obj, name)
    def __hash__(self):
        return hash(self.obj)

def get_equivalent(container, item, default=None):
    '''Gets the specific container element matched by: "item in container".

    Useful for retreiving a canonical value equivalent to "item".  For example, a
    caching or interning application may require fetching a single representative
    instance from many possible equivalent instances).
    '''
    t = _CaptureEq(item)
    if t in container:
        return t.match
    return default