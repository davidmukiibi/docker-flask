import os
from buckeT import app, api
from buckeT.bucketlist import RegisterUser, LoginUser, Bucketlist, BucketlistItem, SingleBucketlist, SingleBucketlistItem


api.add_resource(RegisterUser, '/auth/register/')
api.add_resource(LoginUser, '/auth/login/')
api.add_resource(Bucketlist, '/bucketlists/')
api.add_resource(SingleBucketlist, '/bucketlists/<int:ID>')
api.add_resource(BucketlistItem, '/bucketlists/<int:ID>/items/')
api.add_resource(SingleBucketlistItem, '/bucketlists/<int:ID_bucket>/items/<int:ID_item>')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
