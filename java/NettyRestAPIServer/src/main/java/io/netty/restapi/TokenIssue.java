package io.netty.restapi;

import com.google.gson.JsonObject;
import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.util.StringUtils;
import redis.clients.jedis.Jedis;

import java.util.Map;

/**
 * Created by SunMyeong Lee on 2016-08-31.
 */
public class TokenIssue extends ApiRequestTemplate {
    private static final JedisHelper helper = JedisHelper.getInstance();

    @Autowired
    private SqlSession sqlSession;

    public TokenIssue(Map<String, String> reqData) {
        super(reqData);
    }

    @Override
    public void requestParamValidation() throws RequestParamException {
        if (StringUtils.isEmpty(this.reqData.get("userNo"))) {
            throw new RequestParamException("userNo이 없습니다.");
        }

        if (StringUtils.isEmpty(this.reqData.get("password"))) {
            throw new RequestParamException("password가 없습니다.");
        }
    }

    public void service() throws ServiceException {
        Jedis jedis = null;
        try {
            Map<String, Object> result = sqlSession.selectOne("users.userInfoByPassword", this.reqData);

            if (result != null) {
                final long threeHour = 60 * 60 * 3;
                long issueDate = System.currentTimeMillis() / 1000;
                String email = String.valueOf(result.get("USERID"));

                JsonObject token = new JsonObject();
                token.addProperty("issueDate", issueDate);
                token.addProperty("expireDate", issueDate + threeHour);
                token.addProperty("email", email);
                token.addProperty("userNo", reqData.get("userNo"));
            }
        }
    }
}
