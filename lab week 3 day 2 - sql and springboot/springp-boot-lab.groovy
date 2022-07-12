
// Spring boot Lab
// Working with Java to create a Rest API
// 


import com.fasterxml.jackson.databind.ObjectMapper
import com.fasterxml.jackson.databind.SerializationFeature
import org.springframework.http.MediaType
import org.springframework.web.bind.annotation.DeleteMapping
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.PostMapping
import org.springframework.web.bind.annotation.PutMapping
import org.springframework.web.bind.annotation.RequestBody
import org.springframework.web.bind.annotation.RequestMapping
import org.springframework.web.bind.annotation.RequestMethod
import org.springframework.web.bind.annotation.ResponseBody

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import java.util.ArrayList;
import java.util.*

class Player
{

  private String name;
  private int health;
  private int points;

  public Player(String name)
  {
    super();
    this.name = name;
  }

  void SetPoints(int points)
  {
    this.points = points;
  }

  void GetPoints(int points)
  {
    return this.points ;
  }

}

@RestController
public class TestController
{

    ArrayList<Player> players = new ArrayList<>();


    TestController()
    {
      this.players = new ArayList();
      Player player1 = new Player("--Mark-2007--");
      Player player2 = new Player("CaptureKing27");
      this.players.add(player1);
      this.players.add(player2);
    }

    @RequestMapping(value="/", method = RequestMethod.GET)
    @ResponseBody
    public String home()
    {
        return "REST Demo in Spring Boot";
    }

    @GetMapping(path="/load", produces = "application/json")
    public String loadPlayers()
    {
    System.out.println("Requested to load players");
    ObjectMapper mapper = new ObjectMapper();
    mapper.enable(SerializationFeature.INDENT_OUTPUT);
    return  mapper.writeValueAsString(players);
    }

    @GetMapping(path="/save", produces = "application/json")
    public String savePlayer(@RequestBody String player)
    {
        System.out.println("Requested to save player");

        Player newplayer1 = mapper.readValue(player.toString(), Player.class);
        students.add(newplayer1);
        return "okay added";
    }

}


@SpringBootApplication
public class Application
{
    public static void main(String[] args)
    {
        SpringApplication.run(Application.class, args);
    }
}
