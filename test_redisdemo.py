import redis

class TestRedisDemo:
    # redis-py 使用 connection pool 来管理对一个 redis server 的所有连接，避免每次建立、释放连接的开销。
    # 默认，每个Redis实例都会维护一个自己的连接池。可以直接建立一个连接池，然后作为参数 Redis，这样就可以实现多个 Redis 实例共享一个连接池
    pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
    rd = redis.Redis(connection_pool=pool)
    
    def test_demo1(self):
        """
        redis string类型
        set(name, value, ex=None, px=None, nx=False, xx=False)
        场景：帖子点击数统计
        :return:
        """
        # 设置初始值为0
        self.rd.set("visit:t1:totals", 0)
        # 每次点击自增1
        for i in range(1, 11):
            self.rd.incr("visit:t1:totals", amount=1)
        
        total = int(self.rd.get("visit:t1:totals"))
        print(total)
        assert total == 10
        
        
        
        
        